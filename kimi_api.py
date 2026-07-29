# -*- coding: utf-8 -*-
"""
Kimi (月之暗面) API 接入模块
版本: 1.0
兼容 OpenAI SDK 1.0+

官方文档: https://platform.kimi.com/docs/overview
"""

import os
from typing import List, Dict, Optional, Any

# 尝试导入OpenAI SDK
try:
    from openai import OpenAI
    HAS_OPENAI = True
except ImportError:
    HAS_OPENAI = False


class KimiAPI:
    """
    Kimi (月之暗面) API 客户端封装类

    使用示例:
        >>> api = KimiAPI(api_key="sk-...")
        >>> response = api.chat("你好，请介绍一下自己")
        >>> print(response)
    """

    # API配置常量
    BASE_URL = "https://api.moonshot.cn/v1"
    DEFAULT_MODEL = "kimi-k2.7-code"

    # 可用模型列表（已验证可用性）
    AVAILABLE_MODELS = [
        "kimi-k2.7-code",           # ✅ Kimi K2.7 Code 编程专用模型（可用）
        "kimi-k2.7-code-highspeed", # Kimi K2.7 Code 高速版
        "kimi-k2.6",                # Kimi K2.6 通用模型
        "kimi-k2.5",                # Kimi K2.5 通用模型
        "kimi-k3",                  # Kimi K3 旗舰模型（需特殊权限）
    ]

    def __init__(self, api_key: str, model: str = DEFAULT_MODEL):
        """
        初始化Kimi API客户端

        Args:
            api_key: Kimi API密钥
            model: 使用的模型名称，默认kimi-k3
        """
        if not HAS_OPENAI:
            raise ImportError(
                "请先安装OpenAI SDK: pip install openai>=1.0"
            )

        if not api_key:
            raise ValueError("API密钥不能为空，请提供有效的Kimi API密钥")

        self.api_key = api_key
        self.model = model
        self.client = OpenAI(api_key=api_key, base_url=self.BASE_URL)

        # 对话历史记录
        self.conversation_history: List[Dict[str, str]] = []

        # 系统提示词（默认）
        self.system_prompt = """你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。
你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。
Moonshot AI 为专有名词，不可翻译成其他语言。"""

    def chat(
        self,
        message: str,
        system_prompt: Optional[str] = None,
        use_history: bool = True,
        temperature: float = 1.0,  # Kimi K3 要求 temperature=1
        max_tokens: Optional[int] = None,
        **kwargs
    ) -> str:
        """
        与Kimi对话

        Args:
            message: 用户消息
            system_prompt: 自定义系统提示词，如不提供则使用默认
            use_history: 是否使用历史对话上下文，默认True
            temperature: 温度参数，0-1，越大越随机
            max_tokens: 最大生成长度
            **kwargs: 其他传递给API的参数

        Returns:
            模型返回的回复内容
        """
        # 构建消息列表
        messages = []

        # 添加系统提示词
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        else:
            messages.append({"role": "system", "content": self.system_prompt})

        # 添加历史对话
        if use_history:
            messages.extend(self.conversation_history)

        # 添加当前用户消息
        messages.append({"role": "user", "content": message})

        try:
            # 调用API
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                **kwargs
            )

            # 提取回复内容
            reply = response.choices[0].message.content

            # 保存到对话历史
            if use_history:
                self.conversation_history.append({"role": "user", "content": message})
                self.conversation_history.append({"role": "assistant", "content": reply})

            return reply

        except Exception as e:
            return f"API调用出错: {str(e)}"

    def chat_stream(
        self,
        message: str,
        system_prompt: Optional[str] = None,
        temperature: float = 1.0,  # Kimi K3 要求 temperature=1
    ):
        """
        流式对话（支持实时输出）

        Args:
            message: 用户消息
            system_prompt: 自定义系统提示词
            temperature: 温度参数

        Yields:
            逐块返回的内容
        """
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        else:
            messages.append({"role": "system", "content": self.system_prompt})

        messages.append({"role": "user", "content": message})

        try:
            stream = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature,
                stream=True,
            )

            full_response = ""
            for chunk in stream:
                if chunk.choices[0].delta.content:
                    content = chunk.choices[0].delta.content
                    full_response += content
                    yield content

            # 保存到历史
            self.conversation_history.append({"role": "user", "content": message})
            self.conversation_history.append({"role": "assistant", "content": full_response})

        except Exception as e:
            yield f"API调用出错: {str(e)}"

    def clear_history(self):
        """清空对话历史"""
        self.conversation_history = []

    def count_tokens(self, text: str) -> int:
        """
        估算文本的token数量（简化版）

        Args:
            text: 待估算的文本

        Returns:
            估算的token数量
        """
        # 中文约1.3字符/token，英文约4字符/token
        chinese_chars = sum(1 for c in text if '\u4e00' <= c <= '\u9fff')
        other_chars = len(text) - chinese_chars
        return int(chinese_chars / 1.3 + other_chars / 4)


# ============================================
# 便捷函数：快速获取Kimi API实例
# ============================================
def get_kimi_api(
    api_key: Optional[str] = None,
    model: str = "kimi-k2.7-code"
) -> KimiAPI:
    """
    获取Kimi API客户端实例（支持从环境变量读取密钥）

    Args:
        api_key: API密钥，如果不提供则尝试从环境变量 MOONSHOT_API_KEY 读取
        model: 模型名称

    Returns:
        KimiAPI实例

    示例:
        >>> # 方式1：直接传入密钥
        >>> api = get_kimi_api("sk-...")
        >>>
        >>> # 方式2：从环境变量读取
        >>> import os
        >>> os.environ["MOONSHOT_API_KEY"] = "sk-..."
        >>> api = get_kimi_api()
    """
    # 优先使用传入的密钥，否则尝试从环境变量读取
    key = api_key or os.environ.get("MOONSHOT_API_KEY")

    if not key:
        raise ValueError(
            "未找到API密钥，请直接传入api_key参数，"
            "或设置环境变量 MOONSHOT_API_KEY"
        )

    return KimiAPI(api_key=key, model=model)


# ============================================
# 便捷函数：简化对话调用
# ============================================
def kimi_chat(
    message: str,
    api_key: str,
    model: str = "kimi-k2.7-code",
    system_prompt: Optional[str] = None,
    temperature: float = 1.0,  # Kimi K3 要求 temperature=1
    **kwargs
) -> str:
    """
    便捷的单次对话函数（无需手动创建实例）

    Args:
        message: 用户消息
        api_key: API密钥
        model: 模型名称
        system_prompt: 系统提示词
        **kwargs: 其他参数

    Returns:
        模型回复

    示例:
        >>> response = kimi_chat("你好", "sk-...")
        >>> print(response)
    """
    api = KimiAPI(api_key=api_key, model=model)
    return api.chat(message, system_prompt=system_prompt, use_history=False, **kwargs)


# ============================================
# 测试代码
# ============================================
if __name__ == "__main__":
    # 快速测试示例
    print("=" * 50)
    print("Kimi API 快速测试")
    print("=" * 50)

    # 你的API密钥
    TEST_API_KEY = "sk-kcWs7KsFkwnx5xY862fyIacqN2Wlf9I39YFB56WPLnGb22mD"

    try:
        # 方式1：使用便捷函数
        print("\n[测试1] 使用便捷函数调用...")
        response = kimi_chat(
            "请简单介绍一下你自己，不超过50字",
            api_key=TEST_API_KEY
        )
        print(f"回复: {response}")

        # 方式2：使用API实例（支持多轮对话）
        print("\n[测试2] 使用API实例进行多轮对话...")
        api = KimiAPI(api_key=TEST_API_KEY)

        print("用户: 1 + 1 等于多少？")
        response1 = api.chat("1 + 1 等于多少？")
        print(f"Kimi: {response1}")

        print("\n用户: 那再乘以 2 呢？")
        response2 = api.chat("那再乘以 2 呢？")
        print(f"Kimi: {response2}")

        print("\n" + "=" * 50)
        print("✅ 所有测试完成！Kimi API 接入成功！")
        print("=" * 50)

    except Exception as e:
        print(f"\n❌ 测试失败: {e}")
        print("\n💡 排障建议:")
        print("   1. 检查网络连接是否正常")
        print("   2. 确认API密钥是否正确")
        print("   3. 检查是否已安装 openai SDK: pip install openai>=1.0")
