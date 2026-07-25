# Working Buffer (Danger Zone Log)

> Captures EVERY exchange after 60% context threshold.
> Survives compaction. Review on recovery.

**Status**: INACTIVE (context below 60%)

---

## How It Works

1. **At 60% context** → CLEAR old buffer, set status ACTIVE
2. **Every message after 60%** → log human message + agent summary
3. **After compaction** → read buffer FIRST, extract important context
4. **Leave buffer as-is** until next 60% threshold

---

## Log

_No entries yet. Buffer activates when context exceeds 60%._

<!-- Format:
## [timestamp] Human
message content

## [timestamp] Agent (summary)
1-2 sentence summary of response + key details
-->

---
[[HOME|🏠 返回首页]]
