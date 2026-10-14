# Production-style local build that mirrors GitHub Pages (Jekyll 3.10 via the github-pages gem).
# The Ruby/gem environment lives outside the repo in %LOCALAPPDATA%\jb (see ../README.md).
#
#   .\build.ps1                      clean production build to %LOCALAPPDATA%\jb\_site
#   .\build.ps1 -Config extra.yml    layer an extra config file on top of _config.yml
#
# To look at the result, serve the built folder with any static server, e.g.
#   python -m http.server 4000 --directory "$env:LOCALAPPDATA\jb\_site"
param(
    [string]$Dest = (Join-Path $env:LOCALAPPDATA 'jb\_site'),
    [string]$Config = ''
)
$ErrorActionPreference = 'Continue'   # ruby writes harmless notices to stderr; judge success by exit code below
$jb = Join-Path $env:LOCALAPPDATA 'jb'
$repo = (Resolve-Path (Join-Path $PSScriptRoot '..\..\..')).Path
$env:PATH = "C:\Ruby32-x64\bin;C:\Ruby32-x64\msys64\ucrt64\bin;C:\Ruby32-x64\msys64\usr\bin;$env:PATH"
$env:BUNDLE_GEMFILE = Join-Path $jb 'Gemfile'
$env:BUNDLE_PATH = Join-Path $jb 'vendor'
$env:JEKYLL_ENV = 'production'

$configs = "$repo\_config.yml"
if ($Config) { $configs = "$configs,$Config" }

if (Test-Path $Dest) { Remove-Item -Recurse -Force $Dest }
Push-Location $jb
try {
    bundle exec jekyll build --source $repo --destination $Dest --config $configs --trace
    $code = $LASTEXITCODE
} finally { Pop-Location }
Write-Host "jekyll exit code: $code"
exit $code
