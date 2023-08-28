# Microsoft Hackathon Data

Data for September 2023 Hackathon on Bible Translation and LLMs

In collaboration with SIL (Summer Institute of Linguistics), Microsoft is hosting a hackathon to explore the use of machine learning to improve the quality of Bible translation (specific tasks will be outlined at the outset of the event).

This repository contains data and code for hitting the ground running.

## Data

The data is a collection of Bible translations in the `data/bibles.csv` file.

## Notebooks

- `notebooks/01_quickstart.ipynb` - Quickstart notebook for getting started with the data, including loading the data, and prompting OpenAI with English and source-text data using LangChain
- `notebooks/99-bibles_provenance.ipynb` - Code used to generate combined and consistent parallel Bible data used in this repository

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

## Contact

For questions about this code or data, please contact [Ryder Wishart](https://github.com/ryderwishart).

For questions about the hackathon, please contact Jeremy Hodes or Mark Woodward (SIL), or Chris Priebe (Microsoft).
