Tests et modules factices

Contexte
--------
Certains tests unitaires dans ce dépôt injectent des modules « factices » (fake) au moment de l'import afin de ne pas exiger l'installation de dépendances optionnelles (par exemple : `sqlalchemy`, `fastapi`) dans l'environnement de test minimal.

Pourquoi ?
---------
- Permet d'exécuter rapidement la suite de tests sans installer des dépendances lourdes.
- Facilite l'intégration dans CI minimal ou environnements isolés.
- Les modules factices fournissent juste les symboles nécessaires aux imports et aux annotations ; ils ne remplacent pas un test d'intégration complet.

Fichiers affectés
-----------------
- `tests/test_db_connection_module.py` : injecte un module `sqlalchemy` minimal (fournit `create_engine`, `sessionmaker`, `Session`) si `sqlalchemy` n'est pas installé.
- `tests/test_user_handler_module.py` : injecte un module `fastapi` minimal (fournit `APIRouter`, `HTTPException`) si `fastapi` n'est pas installé.

Comment exécuter les tests
-------------------------
- Exécution rapide (Windows PowerShell) :

```powershell
cd c:\DEV\python-starter-template
python -m pytest -q
```

Recommandations
---------------
- Pour des tests plus réalistes, installez les dépendances :

```powershell
pip install -e .[dev]
# ou
pip install sqlalchemy fastapi pytest-asyncio
```

- Si vous préférez supprimer les modules factices, installez les dépendances et retirez les blocs d'injection dans les fichiers de test.

Notes
-----
Les modules factices sont destinés uniquement aux tests unitaires. Pour les tests d'intégration ou E2E, installez et utilisez les bibliothèques réelles.
