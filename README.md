# Dragon Orchestrator

Skrypt pobiera wskazany sprint, dolacza prompty z `agents` i przekazuje
calosc do Copilot CLI przez standardowe wejscie (takze na Windows).
Kolejnoscia pracy zarzadza model zgodnie z promptem orkiestratora,
nie osobny silnik workflow w Pythonie.

## Uruchomienie

W katalogu projektu, po instalacji i zalogowaniu Copilot CLI:

```powershell
python .\dragon_orchestrator.py --dry-run
python .\dragon_orchestrator.py
python .\dragon_orchestrator.py "URL_WSKAZANEGO_SPRINTU"
```

Bez adresu skrypt korzysta z `DEFAULT_URL` w pliku Python.
`--dry-run` tylko wyswietla prompt. Zwykle uruchomienie automatycznie
zezwala na narzedzia (`--allow-all-tools`), wiec moze zmieniac pliki
i wykonywac polecenia. `--allow-all` dodatkowo znosi ograniczenia sciezek
i adresow; zadna z tych opcji nie tworzy sandboxa.

## Praca przyrostowa

Kazde uruchomienie rozpoczyna nowa sesje CLI; stan poprzednich etapow
pozostaje w kodzie, testach i dokumentacji katalogu `dragon`.
Instrukcje wymagaja rozwijania tego stanu bez podgladania innych sprintow.
Pliki w `agents` to prompty przekazywane modelowi, nie automatycznie
zarejestrowane profile agentow CLI; wykonanie delegacji zalezy od modelu
i dostepnosci narzedzi.

## Testy bez wywolywania modelu

```powershell
python -B -m unittest discover -s .\dragon -p "test_*.py" -v
```
