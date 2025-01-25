# [Architecture](https://github.com/scribe-org/Organization/blob/main/ARCHITECTURE.md)

This markdown file documents the architecture for the whole of [Scribe](https://github.com/scribe-org) - including the applications, the services, the processes, and the external systems and sources with which it interacts. As the file is meant to be a living document, edits are welcome to expand and update it!

<a id="contents"></a>

## Contents

- [Full architecture diagram](#full-architecture)
- [Current architecture diagram](#current-architecture)

<a id="full-architecture"></a>

## Full architecture diagram [`⇧`](#contents)

The following diagram represents the relationships between the Scribe projects and external systems and sources, as they relate to the development plans for Scribe. In other words, the shown architecture depicts a future state for Scribe, which is subject to revision if plans for Scribe change.

```mermaid
    graph RL
        %%%%
        %% ENTITIES

        %% Scribe clients
        IOS([Scribe-iOS])
        ADR([Scribe-Android])
        DSK([Scribe-Desktop])

        %% Client dependencies
        I18N(Scribe-i18n)

        %% Scribe data/service
        API{{Scribe-Server API}}
        DBS[(Scribe-Server DB)]
        DAT[[Scribe-Data]]

        %% Data sources
        WKD[(Wikidata)]
        WKP[(Wikipedia)]
        HGF{{Hugging Face}}
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
                DAT
            end
        end

        %%%%
        %% DATA FLOW

        I18N --->|Provides localization data| IOS & ADR & DSK
        API --->|Client requests data| IOS & ADR & DSK
        DBS --->|API queries for data| API
        DAT --->|Job loads data| DBS
        WKD & WKP & HGF & UNI --->|Job extracts data| DAT
```

<a id="current-architecture"></a>

## Current architecture diagram [`⇧`](#contents)

The following diagram represents the relationships between the Scribe projects and external systems and sources, as they relate to the current state for Scribe. In other words, the diagram is meant to receive more frequent edits, as the intent for it is to accompany the evolution of the Scribe architecture.

```mermaid
    graph BT
        %%%%
        %% ENTITIES

        %% Scribe codebase
        IOS(Scribe-iOS codebase)

        %% Scribe ETL process
        DAT[[Scribe-Data]]

        %% Data sources
        WKD[(Wikidata)]
        WKP[(Wikipedia)]
        HGF{{Hugging Face}}
        UNI((Unicode))

        %% Local development
        DEV[/Scribe developer\]
        subgraph LDM [Local dev machine]
            IOS
            DAT
        end

        %%%%
        %% FLOW

        DEV o-.-o|Dev manually runs ETL| DAT
        WKD & WKP & HGF & UNI --->|ETL extracts data| DAT
        DAT -->|ETL loads data| IOS
```

The architecture diagrams above were created using [mermaid](https://github.com/mermaid-js/mermaid), the diagramming tool with rendering supported in GitHub markdown.
