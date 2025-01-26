# [Data Contracts](https://github.com/scribe-org/Organization/blob/main/DATA_CONTRACTS.md)

> [!NOTE]
> Those new to [Wikidata](https://www.wikidata.org/wiki/Wikidata) should consider first reading the [Wikidata and Scribe Guide](https://github.com/scribe-org/Organization/blob/main/WIKIDATAGUIDE.md).

Scribe uses community curated data from [Wikidata](https://www.wikidata.org/wiki/Wikidata) in all applications via the [Scribe-Data CLI](https://github.com/scribe-org/Scribe-Data). To make sure that Scribe-Data is easy to maintain, we've made the decision that data output labels reflect the data that comprises them. As the data in [Wikidata](https://www.wikidata.org/wiki/Wikidata) can change, that also means that labels can change, meaning that return values for Scribe applications cannot be hard coded. If they were hard coded, then we'd need to update end applications each time that there's new data or the data changes meaning that we wouldn't have parallel update processes for applications and data.

Data labels are generated from underlying data via the [Scribe-Data metadata files](https://github.com/scribe-org/Scribe-Data/tree/main/src/scribe_data/resources) that then are used to check outputs. An example of labels for data coming from the data itself is:

- For a verbs query we check [Wikidata](https://www.wikidata.org/wiki/Wikidata) and see that a verb has the following entities for an `indicative`, `present tense`, `first person`, `singular` conjugation form
  - This verb form for `to go` in French would be `je vais`, in German `ich gehe`, etc
- The Wikidata QIDs for the above entities are [Q682111](https://www.wikidata.org/wiki/Q682111), [Q192613](https://www.wikidata.org/wiki/Q192613), [Q21714344](https://www.wikidata.org/wiki/Q21714344), and [Q110786](https://www.wikidata.org/wiki/Q110786)
- The meta data files determine the translation of QIDs to unique labels and further their order
- The above conjugation would thus be `indicativePresentFirstPersonSingular`
- With similar translations we get all conjugations for a tense:
  - `indicativePresentFirstPersonSingular`
  - `indicativePresentSecondPersonSingular`
  - `indicativePresentThirdPersonSingular`
  - `indicativePresentFirstPersonPlural`
  - `indicativePresentSecondPersonPlural`
  - `indicativePresentThirdPersonPlural`
- The above comprises what the user would see in a conjugation view in a Scribe application

This process has countless benefits for [Scribe-Data](https://github.com/scribe-org/Scribe-Data) as it allows us to check that queries are correct, to get consistent data from [Wikidata](https://www.wikidata.org/wiki/Wikidata) via dumps or the [Wikidata Query Service](https://query.wikidata.org/) and also to generate queries from Wikidata dumps.

But what if the data changed? Data on Wikidata is modeled by a diverse community, meaning not all data is modeled the same, and sometimes it does change. An example of this is nouns in Spanish, where for many languages on Wikidata different genders of a word have their own unique `LID` identifier - `brother` and `sister` would have their own identifiers. At time of writing `brother` and `sister` are on the same identifier in Spanish. We thus need special processes for dealing with Spanish data, but then if we hard coded them and the data changes, then the end applications would break.

A similar situation could arise for conjugations like those above. Say the data was modeled without `indicative` at first, and then the community decides that verbs for a certain language need to include their grammatical mood (`indicative` is a mood). Our applications would be coded to accept `presentFirstPersonSingular`, `presentSecondPersonSingular`, etc, but then all of this would then be broken as the data labels would change.

The solution to this is the [data contracts](https://github.com/scribe-org/Scribe-Data/tree/main/src/scribe_data/wikidata/data-contracts). [Scribe-Data](https://github.com/scribe-org/Scribe-Data) generates both data and the corresponding contracts, with both then being transmitted from [Scribe-Server](https://github.com/scribe-org/Scribe-Server) to end applications. The contracts dictate which columns in which tables should be used to access features for end applications, or combinations of data can be codified so that end applications always know which queries they need to run on the SQLite databases. We run checks to make sure that the current contracts are valid given new data, and if the data changes then we just update the contract values.
