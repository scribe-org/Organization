# Architecture

```mermaid
    graph RL
        %%%%
        %% ENTITIES

        %% Scribe clients
        IOS([Scribe-iOS])
        ADR([Scribe-Android])
        DSK([Scribe-Desktop])

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

        API --->|Client requests data| IOS & ADR & DSK
        DBS --->|API queries for data| API
        DAT --->|Job loads data| DBS
        WKD & WKP & HGF & UNI --->|Job extracts data| DAT
```
