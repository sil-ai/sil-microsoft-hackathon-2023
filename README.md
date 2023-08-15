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

## Contact

For questions about this code or data, please contact [Ryder Wishart](https://github.com/ryderwishart).

For questions about the hackathon, please contact Jeremy Hodes or Mark Woodward (SIL), or Chris Priebe (Microsoft).
