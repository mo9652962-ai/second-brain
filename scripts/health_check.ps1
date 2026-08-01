$os = Get-CimInstance Win32_OperatingSystem
$total = [math]::Round($os.TotalVisibleMemorySize/1MB, 1)
$free = [math]::Round($os.FreePhysicalMemory/1MB, 1)
$used = [math]::Round($total - $free, 1)
$pct = [math]::Round($used/$total*100, 1)
Write-Output ("MEM_TOTAL_GB=" + $total)
Write-Output ("MEM_USED_GB=" + $used)
Write-Output ("MEM_FREE_GB=" + $free)
Write-Output ("MEM_USED_PCT=" + $pct)
$cpu = (Get-CimInstance Win32_Processor | Measure-Object -Property LoadPercentage -Average).Average
Write-Output ("CPU_LOAD_PCT=" + $cpu)
Write-Output "---PROCS---"
Get-Process | Where-Object { $_.ProcessName -match 'hermes|node|python|electron' } |
  Select-Object ProcessName, Id, @{N='MemMB';E={[math]::Round($_.WorkingSet64/1MB,0)}}, StartTime |
  Sort-Object MemMB -Descending | Format-Table -AutoSize | Out-String -Width 200
Write-Output "---UPTIME---"
$uptime = (Get-Date) - $os.LastBootUpTime
Write-Output ("UPTIME_DAYS=" + [math]::Round($uptime.TotalDays, 1))
