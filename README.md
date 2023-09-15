# Microsoft Hackathon Data

Data for September 2023 Hackathon on Bible Translation and LLMs

In collaboration with SIL (Summer Institute of Linguistics), Microsoft is hosting a hackathon to explore the use of machine learning to improve the quality of Bible translation (specific tasks will be outlined at the outset of the event).

This repository contains data and code for hitting the ground running.

## Introductory Presentations

[SIL-Microsoft Hackathon: Introduction to Bible Translation and Project 1](https://docs.google.com/presentation/d/1N_cfJPq36Wc-5c5HD1GnZkC4ruV7Ppitft9YrDXsAh8)

[Assisted Translation using AI (Ryder Wishart)](https://docs.google.com/presentation/d/1KuW7Xu6fS9JhR1RrqUp1khON0C0dUk5uYTc5E-qnQhI/edit?usp=sharing)

[Tokenization of low-resource languages (Ryder Wishart, Bethany Moore, Matthew Shannon)](https://docs.google.com/presentation/d/12G54_PQlyXFuKdjtDfoNe_8RoOtPmdsSSW6g2CHxWvo/edit?usp=sharing)

## Data

The data is a collection of Bible translations in the `data/bibles.csv` file.

## Notebooks

- `notebooks/01_quickstart.ipynb` - Quickstart notebook for getting started with the data, including loading the data, and prompting OpenAI with English and source-text data using LangChain
- `notebooks/99-bibles_provenance.ipynb` - Code used to generate combined and consistent parallel Bible data used in this repository

## Installation
```
# Create a virtual environment (optional) and activate it
python3 -m venv venv
source venv/bin/activate

# install all the requirments
pip install -r requirements.txt

```


## Credits

Greek and Hebrew data is sourced from [Clear-Bible/macula-greek](https://github.com/Clear-Bible/macula-greek/) and [Clear-Bible/macula-hebrew](https://github.com/Clear-Bible/macula-hebrew) respectively.

Parallel English Bibles sourced from [scrollmapper/bible_databases](https://github.com/scrollmapper/bible_databases).

VREF metadata file sourced from [BibleNLP/ebible](https://github.com/BibleNLP/ebible/tree/main). (Many more languages aligned to the metadata file can be found in this eBible repository.)

## License

MIT License

### Translations in the eBible Corpus that have the most permissive licenses (by and by-sa)

The following language codes have highly permissive licenses (including derivative and commercial uses):

```python
['aka', 'amo', 'arbnav', 'asmfb', 'ben2017', 'beo', 'bsj', 'cebulb', 'ckb', 'cmnfeb', 'deu1951', 'dji', 'dov', 'eng-t4t', 'engf35', 'engfbv', 'englsv', 'engourb', 'engtcent', 'engULB', 'ewe', 'francl', 'guj2017', 'gux', 'guxg', 'hatbsa', 'hausa', 'hauulb', 'hin2017', 'hun', 'iloulb', 'indags', 'isn', 'jid', 'jni', 'kan2017', 'kbq', 'kik', 'kiz', 'lin', 'lit', 'lug', 'luo', 'mal', 'malc', 'mar', 'ndg', 'npiulb', 'nya', 'ory', 'pan', 'polsz', 'porblt', 'porbr2018', 'portft', 'reg', 'rmyArli', 'rmyChergash', 'rmyGurbet', 'ronBayash', 'ronludari', 'row', 'sanasm', 'sanben', 'sanbur', 'sandev', 'sanguj', 'sanhk', 'sanias', 'saniso', 'sanitr', 'sankhm', 'sanmal', 'sanori', 'sanpun', 'sansin', 'santam', 'santel', 'santha', 'santib', 'sanurd', 'sanvel', 'sbk', 'sbs', 'spabes', 'spapddpt', 'spavbl', 'swhonen', 'swhulb', 'tam2017', 'tczchongthu', 'tel2017', 'tglulb', 'thd', 'twi', 'uigara', 'uigcyr', 'uiglat', 'uigpin', 'urd', 'vieovcb', 'wbi', 'yij', 'yor', 'zgam']
```

For more detail on each of these, see `data/permissive_licensed_translations.csv`.

### Focus language for the hackathon

For the hackathon translation task, we will focus on the Amo New Testament, since we do not have an Old Testament for this language yet.

The Amo language is a Niger-Congo language from Nigeria. More info may be found at [ethnologue](https://www.ethnologue.com/language/amo/) and [language-archives.org](http://www.language-archives.org/language/amo).

The text for this language can be found in the BibleNLP repo [here](https://github.com/BibleNLP/ebible/blob/main/corpus/amo-amo.txt), and a verse-aligned version with the Greek/Hebrew ([Macula Greek](https://github.com/Clear-Bible/macula-greek/tree/main) and [Hebrew](https://github.com/Clear-Bible/macula-hebrew/tree/main) data) and English ([Berean Standard Bible](https://berean.bible/downloads.htm)) can be found under `data/amo.json`.

The verse-aligned file content contains a JSON array of triplet objects like this:

```json
{
    "vref": "REV 22:21",
    "bsb": {
        "content": "The grace of the Lord Jesus be with all the saints. Amen."
    },
    "macula": {
        "content": "Ἠ  χάρις  τοῦ  Κυρίου  Ἰησοῦ  μετὰ  πάντων."
    },
    "target": {
        "content": "Na nshew nCikilari Yisa so nin ko ngna mine. Uso nani."
    }
}
```

> Note that the `amo.json` file will not have an empty string in `target['content']` for the entire Old Testament. At least, it will until you populate that content!

Because we will not be able to comprehend the output of any generated translations, we will need to rely on techniques such as witholding test data from the New Testament, or other validation methods you might come up with.

## Contact

For questions about this code or data, please contact [Ryder Wishart](https://github.com/ryderwishart).

For questions about the hackathon, please contact Jeremy Hodes or [Mark Woodward](https://github.com/woodwardmw) (SIL), or Chris Priebe (Microsoft).
