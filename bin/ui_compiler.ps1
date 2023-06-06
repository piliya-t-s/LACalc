$targetFolder = "/view/res/"
$fullPath = Join-Path -Path $PWD -ChildPath $targetFolder
$files = Get-ChildItem -Path $fullPath -Recurse -Filter "*.ui"

# get the PyCharm venv activated
$venvActivateScript = "venv\Scripts\activate.ps1"
Invoke-Expression -Command $venvActivateScript

foreach ($file in $files) {
    $outputFileName = "ui_" + $file.Name.Replace(".ui", ".py")
    $command = "pyside6-uic $($file.FullName) -o $($file.Directory.FullName)\$outputFileName"

    Write-Host "Running command: $command"

    Invoke-Expression $command
}
