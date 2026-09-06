# [Architecture](https://github.com/scribe-org/Organization/blob/main/ARCHITECTURE.md)

This markdown file documents the architecture for the whole of [Scribe](https://github.com/scribe-org) - including the applications, the services, the processes and the external systems and sources with which it interacts. As the file is meant to be a living document, edits are welcome to expand and update it!

> [!NOTE]
> You can see the architecture diagram for the [Scribe-Data](https://github.com/scribe-org/Scribe-Data) CLI [here](https://github.com/scribe-org/Scribe-Data/blob/main/ARCHITECTURE.md).

## Architecture Diagram

The following diagram represents the relationships between the Scribe projects and external systems and sources, as they relate to the development plans for Scribe. In other words, the shown architecture depicts the complete state for Scribe, which is subject to revision if plans for Scribe change.

```mermaid
graph RL
    %% Scribe client applications
    IOS([Scribe-iOS\nkeyboard and conjugate\napplications])
    ADR([Scribe-Android\nkeyboard and conjugate\napplications])
    DSK([Scribe-Desktop])

    %% Client dependencies
    I18N(Scribe-i18n)

    %% Scribe data/service
    API{{Scribe-Server API}}
    DBS[(Scribe-Server DB)]
    DATA[[Scribe-Data]]

    %% Data sources
    WD[(Wikidata)]
    WKTN[(Wiktionary)]
    UNI((Unicode))

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

    %% DATA FLOW
    I18N --->|Provides localization data| IOS & ADR & DSK
    API --->|Client requests data| IOS & ADR & DSK
    DBS --->|API queries for data| API
    DATA --->|Job loads data| DBS
    WD & WKTN & UNI --->|Job extracts data| DATA
```

> [!NOTE]
> The architecture diagram above was created using [Mermaid](https://github.com/mermaid-js/mermaid), the diagramming tool with rendering supported in GitHub markdown.
