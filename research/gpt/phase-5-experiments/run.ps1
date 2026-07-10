$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    $python = Get-Command py -ErrorAction SilentlyContinue
}
if (-not $python) {
    throw 'Python 3.10+ must be available as python or py.'
}

& $python.Source -m unittest discover -s tests -p 'test_*.py'
& $python.Source code/run_experiment.py
