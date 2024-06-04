# Wikidata and Scribe Guide

[Wikidata](https://www.wikidata.org/) is a project from the [Wikimedia Foundation](https://www.wikimedia.org/) - Specifically [Wikimedia Deutschland](https://www.wikimedia.de/) (the German chapter of Wikimedia). Like Wikimedia's flagship project [Wikipedia](https://www.wikipedia.org/), [Wikidata](https://www.wikidata.org/) is an open information platform that anyone can edit. More specifically [Wikidata](https://www.wikidata.org/) is an open knowledge graph that is situated in the heart of the [Linked Open Data](https://en.wikipedia.org/wiki/Linked_data) infrastructure that seeks to harness the internet to create a global database of public information that anyone can use.

[Wikidata](https://www.wikidata.org/) data is licensed [CC0](https://creativecommons.org/publicdomain/zero/1.0/) meaning [reuse is permitted with no restriction for personal and commercial purposes](https://creativecommons.org/publicdomain/zero/1.0/). Even though you can use [Wikidata](https://www.wikidata.org/) data without giving credit, we at Scribe suggest that you actively promote your use of [Wikidata](https://www.wikidata.org/) and join the Linked Open Data movement so that all can benefit from the wealth of information created by its dedicated supporters.

Scribe uses [Wikidata](https://www.wikidata.org/) - specifically the [lexicographical data](https://www.wikidata.org/wiki/Wikidata:Lexicographical_data) - as a source of language data via [Scribe-Data](https://github.com/scribe-org/Scribe-Data) and [Scribe-Server](https://github.com/scribe-org/Scribe-Server). All the noun genders, verb conjugations and so much more come directly from Wikidata contributors 💙

This markdown file provides important information about [Wikidata](https://www.wikidata.org/) that is geared towards people interested in learning about it in relation to working on Scribe applications. Edits are welcome to expand and change this document as the community sees fit!

<a id="contents"></a>

# **Contents**

- [First steps into Wikidata](#first-steps)
  - [Data structure](#data-structure)
  - [SPQARL](#spaqrl)
  - [First queries](#first-queries)
  - [Lexeme queries](#lexeme-queries)
- [Scribe-Data and Wikidata](#scribe-data)
- [Scribe-Server and Wikidata](#scribe-server)
- [Further resources](#further-resources)

<a id="first-steps"></a>

# First Steps into Wikidata [`⇧`](#contents)

An important distinction to make is that [Wikidata](https://www.wikidata.org/) is an instance of [Wikibase](https://wikiba.se/) - an open source software for creating collaborative knowledge bases. Wikimedia Deutschland also serves other [Wikibase](https://wikiba.se/) instances such as those found on [Wikibase Cloud](https://www.wikibase.cloud/) that are hosted and [Wikibase Suite](https://www.mediawiki.org/wiki/Wikibase/Docker) that provides [dockerized](https://www.docker.com/) versions of the software for self hosting.

<a id="data-structure"></a>

### Data structure [`⇧`](#contents)

[Wikidata](https://www.wikidata.org/) and other [Wikibase](https://wikiba.se/) instances are not relational databases, but rather [RDF (Resource Description Framework)](https://en.wikipedia.org/wiki/Resource_Description_Framework) graph databases known as [triplestores](https://en.wikipedia.org/wiki/Triplestore). RDF is a directed graph composed of triple statements that include:

1. A subject (the entity being related)
2. A predicate (the relation between the subject and object)
3. An object (the entity being related to)

Note that objects can be a literal value (int, string, date, etc) or another entity within the graph. In [Wikidata](https://www.wikidata.org/) subjects and non-literal objects are generally stored as [QIDs](https://www.wikidata.org/wiki/Q43649390) and predicates are stored as PIDs (see the [Further resources](#further-resources) section for the documentation for [Wikidata](https://www.wikidata.org/) identifiers). Scribe specifically uses Lexemes that are represented as LIDs where each [lemma](<https://en.wikipedia.org/wiki/Lemma_(morphology)>) (base of a word) is given one unique identifier.

A few examples of triples are the following:

- Germany (subject - [Q183](https://www.wikidata.org/wiki/Q183)) has the capital (predicate - [P36](https://www.wikidata.org/wiki/Property:P36)) Berlin (object - [Q64](https://www.wikidata.org/wiki/Q64)).
- Berlin (subject - [Q64](https://www.wikidata.org/wiki/Q64)) has population (predicate - [P1082](https://www.wikidata.org/wiki/Property:P1082)) 3.7 million (object - an integer).
- The European Union (subject - [Q458](https://www.wikidata.org/wiki/Q458)) has the member (predicate - [P527](https://www.wikidata.org/wiki/Property:P527)) Germany (object - [Q183](https://www.wikidata.org/wiki/Q183)).
- Germany (subject - [Q183](https://www.wikidata.org/wiki/Q183)) is a member of (predicate - [P463](https://www.wikidata.org/wiki/Property:P463)) the European Union (object - [Q458](https://www.wikidata.org/wiki/Q458)).

One of the main benefits of RDF triplestores is that there are no limits based on the current structure of the data. If a new relationship is needed, then a predicate for it can be made and the associated objects can then be linked to their subjects.

When comparing to conventional data structures, it's important to mark the distinction that [Wikidata](https://www.wikidata.org/) data is not stored in tables. There are [regular dumps of Wikidata](https://www.wikidata.org/wiki/Wikidata:Database_download) that also come in relational database forms (with `subject`, `predicate` and `object` columns) as well as JSON and other types, but the data on [Wikidata](https://www.wikidata.org/) is stored using RDF relationships.

<a id="spaqrl"></a>

### SPARQL [`⇧`](#contents)

Because the structure of [Wikidata](https://www.wikidata.org/) data is different from traditional relational databases, we also need a different way to query it. [SPARQL](https://en.wikipedia.org/wiki/SPARQL) - the [recursive acronym](https://en.wikipedia.org/wiki/Recursive_acronym) being "SPARQL Protocol and RDF Query Language" - is a standard of querying RDF formatted data.

Another interesting part of SPARQL is that it's also an HTTP transport protocol, so federated queries can also be written that access distributed resources across multiple different SPARQL endpoints. In this way [Wikidata](https://www.wikidata.org/) can be linked to other [Wikibase](https://wikiba.se/) instances or other databases within the linked open data infrastructure.

Note that there are also [aggregation functions](https://en.wikibooks.org/wiki/SPARQL/Aggregate_functions) for SPARQL as in any query language. The only usage of aggregation functions for Scribe is [check_language_data.sparql](https://github.com/scribe-org/Scribe-Data/blob/main/src/scribe_data/check_language_data.sparql) within [Scribe-Data](https://github.com/scribe-org/Scribe-Data). This query allows us to get the totals for categories of words like nouns, verbs and others on a per language basis. The results allow the team to check the overall coverage for the language within [Wikidata](https://www.wikidata.org/) lexemes to prioritize which languages to implement next.

<a id="first-queries"></a>

### First queries [`⇧`](#contents)

Below we find the most common [Wikidata](https://www.wikidata.org/) example of [Q42 - Douglas Adams](https://www.wikidata.org/wiki/Q42), who was specifically given this in homage to his book [The Hitchhiker's Guide to the Galaxy](https://en.wikipedia.org/wiki/The_Hitchhiker%27s_Guide_to_the_Galaxy) in which the "Ultimate Question of Life, the Universe, and Everything" is found to be the number 42 :)

<div align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/a/ae/Datamodel_in_Wikidata.svg" width=1024 alt="Scribe Logo">
</div>

Please go to the [Wikidata Query Service](https://query.wikidata.org/) and try out the following queries to get information about Douglas Adams. You can also click the section header to go directly to the query service with the query populated.

#### [Books that he (Q42) is the author (P50) of](https://w.wiki/AHCb)

```
SELECT
    ?book
    ?bookLabel
    ?bookDescription

WHERE {
    # Subject  # Author  # Douglas Adams
    ?book      wdt:P50   wd:Q42.

    SERVICE wikibase:label { bd:serviceParam wikibase:language
    "[AUTO_LANGUAGE], en". }
}
```

> [!NOTE]\
> The Scribe team would strongly suggest that VS Code developers download the [Wikidata QID Labels VS Code extension](https://marketplace.visualstudio.com/items?itemName=blokhinnv.wikidataqidlabels) that provides an in editor tooltip for Wikidata ID labels.

It's important to note that for triples where the object is a [Wikidata](https://www.wikidata.org/) entity the response to queries is its unique ID, not the string label. In order to get labels for our results we need to add in the labeling service to our queries that will then give us the ability to create any `colNameLabel` column for a column of IDs `colName`. We add this service via the following line that sets English as the default returned value at the end:

```
SERVICE wikibase:label { bd:serviceParam wikibase:language
  "[AUTO_LANGUAGE], en". }
```

Note that `?colNameDescription` functions in a similar way where the description of the ID can be returned.

#### [His (Q42) date of birth (P569)](https://w.wiki/8jHg)

> [!NOTE]\
> We don't need to call the label service in this query as the object isn't a Wikidata entity.

```
SELECT
    ?dateOfBirth

WHERE {
    # Douglas Adams  # Date of Birth  # Object
    wd:Q42           wdt:P569         ?dateOfBirth.
}
```

#### [His (Q42) place of birth (P19)](https://w.wiki/AHCc)

```
SELECT
    ?placeOfBirth
    ?placeOfBirthLabel

WHERE {
    # Douglas Adams  # Place of Birth  # Object
    wd:Q42           wdt:P19           ?placeOfBirth.

    SERVICE wikibase:label { bd:serviceParam wikibase:language
    "[AUTO_LANGUAGE], en". }
}
```

#### [All people (Q5) with the same place of birth (P19) as him (Q42)](https://w.wiki/AHCX)

```
SELECT DISTINCT
    ?person
    ?personLabel
    ?personDescription

WHERE {
    # Douglas Adams  # Place of Birth  # Object
    wd:Q42           wdt:P19           ?placeOfBirth.
    # Subject  # Instance of  # Human
    ?person    wdt:P31        wd:Q5;
               # Place of birth/*  # Object
               wdt:P19/wdt:P131*   ?placeOfBirth;

    SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en" }
}
```

Here's one more query to try out on the [Wikidata Query Service](https://query.wikidata.org). Can you change it to get different results? The following are great ways to find the [Wikidata](https://www.wikidata.org/) IDs you're looking for to rewrite the query below:

- Search for the main item on [Wikidata](https://www.wikidata.org/) (in this case [the European Union](https://www.wikidata.org/wiki/Q458))
  - Check statements on the left and navigate to their PIDs
- Use a search engine to search for `Wikidata NAME_OF_ITEM`, with the first result normally being the correct one
- Use the [Wikidata Query Builder](https://www.wikidata.org/wiki/Wikidata:Query_Builder) to construct your query from normal language

#### [All countries that are members of (P463) the European Union (Q458)](https://w.wiki/AHCe)

```
SELECT
    ?country
    ?countryLabel

WHERE {
    # Subject  # Member of  # The European Union
    ?country   wdt:P463     wd:Q458.

    SERVICE wikibase:label { bd:serviceParam wikibase:language
    "[AUTO_LANGUAGE], en". }
}
```

<a id="lexeme-queries"></a>

### Lexeme queries [`⇧`](#contents)

The focus now shifts to the kind of data that's of interest to Scribe. [Wikidata](https://www.wikidata.org/) [lexicographical data](https://www.wikidata.org/wiki/Wikidata:Lexicographical_data) maps out lemmas (base versions of words) as LIDs and attaches all forms of the lemma as queryable points of data. Let's start with a base query:

#### [Query ten German (Q188) nouns (Q1084)](https://w.wiki/AHCi)

```
SELECT DISTINCT
    ?lexeme
    ?lemma

WHERE {
    # Subject            # German
    ?lexeme dct:language wd:Q188 ;
        # Predicate              # Noun
        wikibase:lexicalCategory wd:Q1084 ;
        # The following is like labels above.
        wikibase:lemma ?lemma .
}

LIMIT 10
```

First we start with a lexeme, then we call the language dictionary to define which language it's from, we then apply a lexical category where we define that we only want nouns, and at the end we ask for the lemma via `wikibase:lemma` (the equivalent of labels for lexemes). Removing `LIMIT 10` would give us the first query of interest to Scribe: all German nouns!

From here we need to get the forms (singular, plural, gender, etc) associated with the noun. Not every lemma is going to have all the points of data as they might not have been added or might not be grammatically valid, so for later steps we wrap form queries in `OPTIONAL` blocks.

#### [Query ten German (Q188) nouns (Q1084) with singulars (Q110786) and plurals (Q146786)](https://w.wiki/AHCj)

```
SELECT DISTINCT
    ?lexeme
    ?lemma
    ?singular
    ?plural

WHERE {
    ?lexeme dct:language wd:Q188 ;
        wikibase:lexicalCategory wd:Q1084 ;
        wikibase:lemma ?lemma .

    OPTIONAL {
        ?lexeme ontolex:lexicalForm ?singularForm .
        ?singularForm ontolex:representation ?singular ;
        wikibase:grammaticalFeature wd:Q110786 ;
    } .

    OPTIONAL {
        ?lexeme ontolex:lexicalForm ?pluralForm .
        ?pluralForm ontolex:representation ?plural ;
        wikibase:grammaticalFeature wd:Q146786 ;
    } .
}

LIMIT 10
```

From here we're able to create most of the queries used by Scribe by changing the language that lexemes should be associated with, the category of word that we need (nouns, verbs, etc) and editing the optional form selections to include all needed information about the lemma that's needed for Scribe applications.

<a id="scribe-data"></a>

# Scribe-Data and Wikidata [`⇧`](#contents)

[Scribe-Data](https://github.com/scribe-org/Scribe-Data) data process that interfaces with [Wikidata's lexicographical data](https://www.wikidata.org/wiki/Wikidata:Lexicographical_data) with the following functionality:

- Defines SPARQL queries with which data can be extracted from [Wikidata](https://www.wikidata.org/)
  - Sometimes queries need to be broken up as there are too many results
- Passes these queries to [Wikidata](https://www.wikidata.org/) via the Python library [SPARQLwrapper](https://github.com/RDFLib/sparqlwrapper)
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

- [Wikidata on Wikipedia](https://en.wikipedia.org/wiki/Wikidata)
- [Wikidata Identifiers](https://www.wikidata.org/wiki/Wikidata:Identifiers)

### Querying Wikidata

- [Wikidata SPARQL tutorial](https://www.wikidata.org/wiki/Wikidata:SPARQL_tutorial)
- [Wikidata tutorial by Wikimedia Israel](https://wdqs-tutorial.toolforge.org/)
- [Wikidata example SPARQL queries](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/queries/examples)
- [Wikidata Query Builder](https://www.wikidata.org/wiki/Wikidata:Query_Builder)
- [Wikidata Query Builder Documentation](https://query.wikidata.org/querybuilder)

### Wikidata lexemes

- [Wikidata lexicographical data](https://www.wikidata.org/wiki/Wikidata:Lexicographical_data)
- [Wikidata example lexeme queries](https://www.wikidata.org/wiki/Wikidata:Lexicographical_data/Ideas_of_queries)
- [Wikidata Lexicographical Data Statistics](https://www.wikidata.org/wiki/Wikidata:Lexicographical_data/Statistics/Counts_of_various_things_by_language)

### Tools used by Scribe

- [SPARQLwrapper Python package](https://github.com/RDFLib/sparqlwrapper)
- [Wikidata QID Labels VS Code extension](https://marketplace.visualstudio.com/items?itemName=blokhinnv.wikidataqidlabels)
