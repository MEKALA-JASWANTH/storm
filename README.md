# FORK MODIFICATIONS

**This is a forked version of the original STORM project with the following changes:**

1. **Updated README**: Added this modifications section to clearly document changes made to the fork
2. **New Sample Module**: Added `sample_feature.py` - a basic sample module demonstrating extensibility
3. **Fork Purpose**: This fork serves as a demonstration of extending the STORM project with custom features

**Original Project**: [Stanford-OVAL/STORM](https://github.com/stanford-oval/storm)

---

<p align="center">  <img src="assets/logo.svg" style="width: 25%; height: auto;"></p>

# STORM: Synthesis of Topic Outlines through Retrieval and Multi-perspective Question Asking

<p align="center">| <a href="http://storm.genie.stanford.edu"><b>Research preview</b></a> | <a href="https://arxiv.org/abs/2402.14207"><b>STORM Paper</b></a>| <a href="https://www.arxiv.org/abs/2408.15232"><b>Co-STORM Paper</b></a>  | <a href="https://storm-project.stanford.edu/"><b>Website</b></a> |</p>

**Latest News** 🔥
- [2025/01] We add [litellm](https://github.com/BerriAI/litellm) integration for language models and embedding models in `knowledge-storm` v1.1.0.
- [2024/09] Co-STORM codebase is now released and integrated into `knowledge-storm` python package v1.0.0. Run `pip install knowledge-storm --upgrade` to check it out.
- [2024/09] We introduce collaborative STORM (Co-STORM) to support human-AI collaborative knowledge curation! [Co-STORM Paper](https://www.arxiv.org/abs/2408.15232) has been accepted to EMNLP 2024 main conference.
- [2024/07] You can now install our package with `pip install knowledge-storm`!
- [2024/07] We add `VectorRM` to support grounding on user-provided documents, complementing existing support of search engines (`YouRM`, `BingSearch`). (check out [#58](https://github.com/stanford-oval/storm/pull/58))
- [2024/07] We release demo light for developers a minimal user interface built with streamlit framework in Python, handy for local development and demo hosting (checkout [#54](https://github.com/stanford-oval/storm/pull/54))
- [2024/06] We will present STORM at NAACL 2024! Find us at Poster Session 2 on June 17 or check our [presentation material](assets/storm_naacl2024_slides.pdf). 
- [2024/05] We add Bing Search support in [rm.py](knowledge_storm/rm.py). Test STORM with `GPT-4o` - we now configure the article generation part in our demo using `GPT-4o` model.
- [2024/04] We release refactored version of STORM codebase! We define [interface](knowledge_storm/interface.py) for STORM pipeline and reimplement STORM-wiki (check out [`src/storm_wiki`](knowledge_storm/storm_wiki)) to demonstrate how to instantiate the pipeline. We provide API to support customization of different language models and retrieval/search integration.
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Overview [(Try STORM now!)](https://storm.genie.stanford.edu/)

<p align="center">  <img src="assets/overview.svg" style="width: 90%; height: auto;"></p>

STORM is a LLM system that writes Wikipedia-like articles from scratch based on Internet search. Co-STORM further enhanced its feature by enabling human to collaborative LLM system to support more aligned and preferred information seeking and knowledge curation.
