# [Architecture](https://github.com/scribe-org/Organization/blob/main/ARCHITECTURE.md)

This markdown file documents the architecture for the whole of [Scribe](https://github.com/scribe-org) - including the applications, the services, the processes, and the external systems and sources with which it interacts. As the file is meant to be a living document, edits are welcome to expand and update it!

## Architecture Diagram

The following diagram represents the relationships between the Scribe projects and external systems and sources, as they relate to the development plans for Scribe. In other words, the shown architecture depicts the complete state for Scribe, which is subject to revision if plans for Scribe change.

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

The architecture diagram above was created using [mermaid](https://github.com/mermaid-js/mermaid), the diagramming tool with rendering supported in GitHub markdown.
