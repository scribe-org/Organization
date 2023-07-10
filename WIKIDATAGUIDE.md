# Wikidata and Scribe Guide

[Wikidata](https://www.wikidata.org/) is a project from the [Wikimedia Foundation](https://www.wikimedia.org/) - Specifically [Wikimedia Deutschland](https://www.wikimedia.de/) (the German chapter of Wikimedia). Like Wikimedia's flagship project [Wikipedia](https://www.wikipedia.org/), [Wikidata](https://www.wikidata.org/) is an open information platform that anyone can edit. More specifically [Wikidata](https://www.wikidata.org/) is an open knowledge graph that is situated in the heart of the [Linked Open Data](https://en.wikipedia.org/wiki/Linked_data) infrastructure that seeks to harness the internet to create a global database of public information that anyone can use.

[Wikidata](https://www.wikidata.org/) data is licensed [CC0](https://creativecommons.org/publicdomain/zero/1.0/) meaning reuse is permitted with no restriction for personal and commercial purposes. Even though you can use [Wikidata](https://www.wikidata.org/) data without giving credit, we at Scribe suggest that you actively promote your use of [Wikidata](https://www.wikidata.org/) and join the Linked Open Data movement so that we all can benefit from the wealth of information created by its dedicated supporters.

Scribe uses [Wikidata](https://www.wikidata.org/) as a source of language data via [Scribe-Data](https://github.com/scribe-org/Scribe-Data), [Scribe-Server](https://github.com/scribe-org/Scribe-Server) and [Wikidata's lexicographical data](https://www.wikidata.org/wiki/Wikidata:Lexicographical_data): so all the noun genders, verb conjugations and so much more come directly from Wikidata contributors ❤️

This markdown file provides important information about [Wikidata](https://www.wikidata.org/) that is geared towards people interested in learning about it in relation to working on Scribe applications. The general information about [Wikidata](https://www.wikidata.org/) with helpful resources can of course be expanded as the community sees fit. Edits are welcome!

<a id="contents"></a>

# **Contents**

- [First steps into Wikidata](#first-steps)
  - [Data structure](#data-structure)
  - [First query](#first-query)
- [Scribe-Data and Wikidata](#scribe-data)
- [Scribe-Server and Wikidata](#scribe-server)
- [Further resources](#further-resources)

<a id="first-steps"></a>

# First Steps into Wikidata [`⇧`](#contents)

<a id="data-structure"></a>

### Data structure [`⇧`](#contents)

<a id="first-query"></a>

### First query [`⇧`](#contents)

<a id="scribe-data"></a>

# Scribe-Data and Wikidata [`⇧`](#contents)

At one point within the Scribe-iOS repository, [Scribe-Data](https://github.com/scribe-org/Scribe-Data) is now a standalone data process that interfaces with [Wikidata's lexicographical data](https://www.wikidata.org/wiki/Wikidata:Lexicographical_data). [Scribe-Data](https://github.com/scribe-org/Scribe-Data) has the following functionality:

- Defines SPARQL queries with which data can be extracted from [Scribe-Data](https://github.com/scribe-org/Scribe-Data)
- Formats extracted data and prepares them for use within Scribe applications
- Creates SQLite databases that form the basis of language packs that are loaded into Scribe app interfaces

Functionality not related to [Wikidata](https://www.wikidata.org/) includes:

- Generating Emoji-trigger word relations for emoji autosuggestions and autocompletions using [Unicode CLDR](https://github.com/unicode-org/cldr) data
- Creating autosuggest dictionaries based on the most frequent words in [Wikipedia](https://www.wikipedia.org/) and the words that most frequently follow them

<a id="scribe-server"></a>

# Scribe-Server and Wikidata [`⇧`](#contents)

[Scribe-Server](https://github.com/scribe-org/Scribe-Server) functions as an automation step that runs [Scribe-Data](https://github.com/scribe-org/Scribe-Data) as a package and automatically updates [Wikidata](https://www.wikidata.org/) based language packs for users to then download within Scribe applications.

<a id="further-resources"></a>

# Further resources [`⇧`](#contents)

The following are other resources that the community suggests to broaden your understanding of [Wikidata](https://www.wikidata.org/) and using it in Scribe development. Some resources from above are repeated to assure that the this section is a comprehensive list.

### Wikidata lexemes

### Querying Wikidata

### Tools used by Scribe
