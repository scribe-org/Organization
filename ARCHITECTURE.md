# [Architecture](https://github.com/scribe-org/Organization/blob/main/ARCHITECTURE.md)

This markdown file documents the architecture for the whole of [Scribe](https://github.com/scribe-org) - including the applications, the services, the processes and the external systems and sources with which it interacts. As the file is meant to be a living document, edits are welcome to expand and update it!

> [!NOTE]
> You can see the architecture diagram for the [Scribe-Data](https://github.com/scribe-org/Scribe-Data) CLI [here](https://github.com/scribe-org/Scribe-Data/blob/main/ARCHITECTURE.md).

## Architecture Diagram

The following diagram represents the relationships between the Scribe projects and external systems and sources, as they relate to the current and long term development plans for Scribe.

```mermaid
graph RL
    subgraph SOURCES [Data sources]
        WD[(Wikidata)]
        WKTN[(Wiktionary)]
        UNI((Unicode))
    end

    %% Scribe data/service
    API{{Scribe-Server API}}
    DBS[(Scribe-Server DB)]
    DATA[[Scribe-Data CLI]]

    %% Toolforge (WMCS)
    subgraph TFP [Toolforge platform]
        subgraph TFW [Toolforge webservice]
            API
        end
        subgraph TDB [ToolsDB]
            DBS
        end
        subgraph TFJ [Toolforge job]
            DATA
        end
    end

    %% Client dependencies
    I18N(Scribe-i18n\nGit submodule)

    subgraph CLIENTS [Scribe client applications]
        IOS([Scribe-iOS\nkeyboard and conjugate\napplications])
        ADR([Scribe-Android\nkeyboard and conjugate\napplications])
        DSK([Scribe-Desktop\nGUI application])
    end

    %% Website
    SCR([scri.be website])

    %% DATA FLOW
    I18N --->|Provides localization data| IOS & ADR & DSK & SCR
    API --->|Client requests language\ndata and contracts| IOS & ADR & DSK
    DBS --->|API queries for data| API
    DATA --->|Job loads data| DBS
    WD --->|Job extracts\nlanguage data| DATA
    WKTN --->|Job extracts\ntranslation data| DATA
    UNI --->|Job extracts\nemoji data| DATA
```

> [!NOTE]
> The architecture diagram above was created using the diagramming tool [Mermaid](https://github.com/mermaid-js/mermaid), with rendering supported in GitHub markdown.
