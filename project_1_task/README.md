# Project 1: AI Question Answering for Quality Checking w/ AQuA and Scripture Forge

Producing high quality Bible translations is critically important in the mission to bring God’s word to every tribe, tongue, and nation.

Bible translators and quality consultants spend long hours carefully scrutinizing every verse as drafts undergo the rigorous quality checking process. Then the draft goes through “community checking” during which local communities contribute significant hours answering questions based on translation drafts to ensure important details have been translated effectively.

This process is one of the most time-consuming tasks in Bible translation and the number of translation consultants available for the work is extremely limited. While nothing can replace the Spirit-led discernment, prayer, and fellowship that quality checking requires, AI technology can serve and aid those teams in a variety of ways.

SIL International’s AQuA (Augmented Quality Assessment) and Scripture Forge tools serve as quality checking co-pilots designed to use AI to help translators, consultants, and communities in their work.

For example, Scripture Forge provides an interface in which translation teams can import Questions & Answers for community checkers to answer. Current open source Question & Answer datasets often do not contain questions for every single verse. Ideally, there should be questions not only for every verse, but multiple questions per verse. AI language models might help generate and evaluate this data ensuring community checking is effective and comprehensive.

Additionally, AQuA provides a handful of AI-driven assessments to score and visualize specific areas of scripture that may require extra or early review. If AI can improve the quality of new drafts before they begin the rigorous quality checking process, or identify potential revisions earlier in that quality checking process, overall efficiency could significantly improve. The AQuA team is currently exploring whether an AI-driven Question Answering model could be developed that would be useful in this way to translators and consultants.

Hackathon tasks:

* Evaluate whether Question Answering models, including ChatGPT and other LLMs, could be used to create a new AQuA assessment, and which might be most useful.
* Generate Q&A datasets by verse (or pericopes or even entire sections) that should be answerable given a new draft or its back translation.
* Evaluate the effectiveness of the Q&A datasets for the given purpose.
* Question-Answer pairs generated for SF community checking may be qualitatively different from those most useful for AQuA’s QA assessment.

Data sources:

* [Ebible Corpus](https://github.com/BibleNLP/ebible)
* [Greek and Hebrew texts](../data/combined_greek_hebrew_vref.csv)
* [MACULA Hebrew data](https://github.com/Clear-Bible/macula-hebrew)
* [MACULA Greek data](https://github.com/Clear-Bible/macula-greek)
* [Pre-hackathon internship work](./pre-Hackathon)

Current QA model used for inference:

[sentence-transformers/all-mpnet-base-v2](https://huggingface.co/sentence-transformers/all-mpnet-base-v2)