# Wikidata and Scribe Guide

[Wikidata](https://www.wikidata.org/) is a project from the [Wikimedia Foundation](https://www.wikimedia.org/) - Specifically [Wikimedia Deutschland](https://www.wikimedia.de/) (the German chapter of Wikimedia). Like Wikimedia's flagship project [Wikipedia](https://www.wikipedia.org/), [Wikidata](https://www.wikidata.org/) is an open information platform that anyone can edit. More specifically [Wikidata](https://www.wikidata.org/) is an open knowledge graph that is situated in the heart of the [Linked Open Data](https://en.wikipedia.org/wiki/Linked_data) infrastructure that seeks to harness the internet to create a global database of public information that anyone can use.

[Wikidata](https://www.wikidata.org/) data is licensed [CC0](https://creativecommons.org/publicdomain/zero/1.0/) meaning [reuse is permitted with no restriction for personal and commercial purposes](https://creativecommons.org/publicdomain/zero/1.0/). Even though you can use [Wikidata](https://www.wikidata.org/) data without giving credit, we at Scribe suggest that you actively promote your use of [Wikidata](https://www.wikidata.org/) and join the Linked Open Data movement so that all can benefit from the wealth of information created by its dedicated supporters.

Scribe uses [Wikidata](https://www.wikidata.org/) - specifically the [lexicographical data](https://www.wikidata.org/wiki/Wikidata:Lexicographical_data) - as a source of language data via [Scribe-Data](https://github.com/scribe-org/Scribe-Data), [Scribe-Server](https://github.com/scribe-org/Scribe-Server). All the noun genders, verb conjugations and so much more come directly from Wikidata contributors ❤️

This markdown file provides important information about [Wikidata](https://www.wikidata.org/) that is geared towards people interested in learning about it in relation to working on Scribe applications. Edits are welcome to expand and change this document as the community sees fit!

<a id="contents"></a>

# **Contents**

- [First steps into Wikidata](#first-steps)
  - [Data structure](#data-structure)
  - [First query](#first-query)
  - [Lexeme query](#lexeme-query)
- [Scribe-Data and Wikidata](#scribe-data)
- [Scribe-Server and Wikidata](#scribe-server)
- [Further resources](#further-resources)

<a id="first-steps"></a>

# First Steps into Wikidata [`⇧`](#contents)

An important distinction to make is that [Wikidata](https://www.wikidata.org/) is an instance of [Wikibase](https://wikiba.se/) - an open source software for creating collaborative knowledge bases. Wikimedia Deutschland also serves other Wikibase instances such as those found on [Wikibase Cloud](https://www.wikibase.cloud/) that are hosted and [Wikibase Suite](https://www.mediawiki.org/wiki/Wikibase/Docker) that provides [dockerized](https://www.docker.com/) versions of the software for self hosting.

<a id="data-structure"></a>

### Data structure [`⇧`](#contents)

Importantly [Wikidata](https://www.wikidata.org/) and other [Wikibase](https://wikiba.se/) instances are not relational databases, but rather [RDF (Resource Description Framework)](https://en.wikipedia.org/wiki/Resource_Description_Framework) graph databases. RDF is a directed graph composed of triple statements that include:

1. A subject (the entity being related)
2. A predicate (the relation between the subject and object)
3. An object (the entity being related to)

Note that objects can be a literal value (int, string, date, etc) or another entity within the graph. In Wikidata subjects and non-literal objects are generally stored as [QIDs](https://www.wikidata.org/wiki/Q43649390) and predicates are stored as PIDs (see the [Further resources](#further-resources) section for the documentation for Wikidata identifiers). Scribe specifically uses Lexemes that are represented as LIDs where each base word is given one unique identifier.

Below we find the most common Wikidata example of [Q42 - Douglas Adams](https://www.wikidata.org/wiki/Q42), who was specifically given this in homage to his book [The Hitchhiker's Guide to the Galaxy](https://en.wikipedia.org/wiki/The_Hitchhiker%27s_Guide_to_the_Galaxy) in which the "Ultimate Question of Life, the Universe, and Everything" is found to be the number 42 :)

<div align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/a/ae/Datamodel_in_Wikidata.svg" width=1024 alt="Scribe Logo">
</div>

When comparing to conventional data structures, it's important to mark the distinction that [Wikidata](https://www.wikidata.org/) data is not stored in tables. There are [regular dumps of Wikidata](https://www.wikidata.org/wiki/Wikidata:Database_download) that also come in relational database forms as well as JSON and other types, but the data on [Wikidata](https://www.wikidata.org/) is stored using RDF relationships.

<a id="first-query"></a>

### First query [`⇧`](#contents)

<a id="lexeme-query"></a>

### Lexeme query [`⇧`](#contents)

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

### Wikidata documentation

- [Wikidata Identifiers](https://www.wikidata.org/wiki/Wikidata:Identifiers)

### Querying Wikidata

### Wikidata lexemes

- [Example lexeme queries](https://www.wikidata.org/wiki/Wikidata:Lexicographical_data/Ideas_of_queries)

### Tools used by Scribe
