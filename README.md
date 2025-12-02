# tryConventionalCommits

Repository di prova per sperimentare e documentare l'uso di Conventional Commits.

**Scopo**

- Permettere di testare formati di commit coerenti (Conventional Commits).
- Mostrare esempi pratici di messaggi e una configurazione minima per linting e hook.

**Perché usare Conventional Commits?**

- Migliora la leggibilità della cronologia dei commit.
- Abilita release automatizzate e generazione di changelog.
- Standardizza il contributo da più sviluppatori.

**Formato base dei messaggi**
Un messaggio di commit seguente il formato Conventional Commits ha questa struttura:

```
<type>(<scope>): <short description>

[optional body]

[optional footer]
```

Esempi:

- `feat(auth): aggiunge login con OAuth`
- `fix(api): corregge gestione degli errori 500`
- `chore: aggiorna dipendenze di sviluppo`

Tipici `type`:

- `feat`: nuova funzionalità
- `fix`: correzione di bug
- `docs`: documentazione
- `style`: formattazione (non influisce al codice)
- `refactor`: refactoring senza cambi funzionali
- `test`: aggiunta o modifica di test
- `chore`: attività di manutenzione
