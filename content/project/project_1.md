{
  "Title": "BIDS: IP-Freely",
  "link_to_issue": "https://github.com/brainhackorg/global2024/issues/1",
  "issue_number": 1,
  "labels": [
    {
      "name": "git_skills:0_none",
      "description": "",
      "color": "5B6C2C"
    },
    {
      "name": "modality:behavioral",
      "description": "",
      "color": "1d76db"
    },
    {
      "name": "modality:DWI",
      "description": "",
      "color": "1d76db"
    },
    {
      "name": "modality:ECG",
      "description": "",
      "color": "1d76db"
    },
    {
      "name": "modality:ECOG",
      "description": "",
      "color": "1d76db"
    },
    {
      "name": "modality:EEG",
      "description": "",
      "color": "1d76db"
    },
    {
      "name": "modality:eye_tracking",
      "description": "",
      "color": "1d76db"
    },
    {
      "name": "modality:fMRI",
      "description": "",
      "color": "1d76db"
    },
    {
      "name": "modality:MEG",
      "description": "",
      "color": "1d76db"
    },
    {
      "name": "modality:MRI",
      "description": "",
      "color": "1d76db"
    },
    {
      "name": "modality:PET",
      "description": "",
      "color": "1d76db"
    },
    {
      "name": "programming:documentation",
      "description": "",
      "color": "5319E7"
    },
    {
      "name": "programming:Python",
      "description": "",
      "color": "5319E7"
    },
    {
      "name": "project",
      "description": "",
      "color": "B60205"
    },
    {
      "name": "project_development_status:0_concept_no_content",
      "description": "",
      "color": "D93F0B"
    },
    {
      "name": "project_tools_skills:expert",
      "description": null,
      "color": "ededed"
    },
    {
      "name": "project_tools_skills:familiar",
      "description": null,
      "color": "ededed"
    },
    {
      "name": "project_type:coding_methods",
      "description": null,
      "color": "ededed"
    },
    {
      "name": "project_type:data_management",
      "description": null,
      "color": "ededed"
    },
    {
      "name": "project_type:documentation",
      "description": null,
      "color": "ededed"
    },
    {
      "name": "status:web_ready",
      "description": "",
      "color": "0E8A16"
    },
    {
      "name": "tools:BIDS",
      "description": "",
      "color": "EA1D4E"
    },
    {
      "name": "topic:reproducible_scientific_methods",
      "description": "",
      "color": "FBCA04"
    },
    {
      "name": "modality:fNIRS",
      "description": null,
      "color": "ededed"
    },
    {
      "name": "modality:TDCS",
      "description": null,
      "color": "ededed"
    },
    {
      "name": "modality:TMS",
      "description": null,
      "color": "ededed"
    }
  ],
  "content": "### Title\n\nFree manipulation of BIDS datasets according to the Inheritance Principle\n\n### Leaders\n\nRobert E. Smith; https://x.com/Lestropie\n\n### Collaborators\n\n_No response_\n\n### Brainhack Global 2024 Event\n\nBrainhack Aus\n\n### Project Description\n\nThe Inheritance Principle (\"IP\") has been a feature of the Brain Imaging Data Structure (BIDS) since its inception. It describes how the metadata relevant to one specific data file may in fact originate from multiple metadata files. Encoding some common metadata field just once, and having it be deemed applicable to multiple metadata files, may both reduce redundancy and communicate the intrinsic hierarchical structure of the dataset. This however comes at considerable complexity to the specification itself and the software responsible for interfacing with such data. Indeed nearly a decade after its creation, many software APIs for parsing BIDS data still do not support the Inheritance Principle.\r\n\r\nThe future of the IP is at a crossroads, particularly as work progresses toward BIDS 2.0:\r\n-   On one hand, some would like for the IP to disappear entirely: all metadata relevant to any given data file would need to be stored in a sidecar metadata file alongside that data file, regardless of duplication.\r\n-   On the other, not just preserving the IP but *augmenting* it could better communicate the complex hierarchical dependencies of complex datasets, particularly derivative data.\r\n\r\nThe goals of this project are twofold.\r\n\r\n1.  There is a dearth of existing software tools for managing the IP. If a dataset that exploits the IP were provided as input to a BIDS App that is naive to the IP, that App could perform improper association of metadata. Existing datasets may contain substantial metadata redundancy, due to not currently having an easy way through which to exploit the IP. A tool to automate such data manipulations could therefore be useful in the BIDS ecosystem.\r\n\r\n2.  Consequential decisions regarding the IP and related issues in BIDS 2.0 would be better informed if stakeholders could see the effects that proposed specifications would have on how compliant datasets appear.\r\n\n\n### Link to project repository/sources\n\nhttps://github.com/Lestropie/IP-freely\n\n### Goals for Brainhack Global\n\n-   Primary goal: Produce one or more exemplar BIDS datasets that exemplify the complexity of the Inheritance Principle, which can therefore be used to demonstrate the influence of its removal or exploitation under different rule sets: https://github.com/Lestropie/IP-freely/issues/5\r\n\r\n-   Primary goal: Take a BIDS dataset that may include use of the Inheritance Principle, and create a new version of that dataset that removes all usage of the Inheritance Principle: https://github.com/Lestropie/IP-freely/issues/1\r\n\r\n-   Primary goal: Take a BIDS dataset that may (but likely does not) include use of the Inheritance Principle, and create a new version of that dataset that makes *maximal* use of the Inheritance Principle (without overloading): https://github.com/Lestropie/IP-freely/issues/2\r\n\r\n-   Secondary goals: Other issues listed at https://github.com/Lestropie/IP-freely/issues.\r\n\n\n### Good first issues\n\nFor anyone not accustomed to open source projects, perhaps the most accessible entrypoint will be the construction of one or more exemplar datasets: https://github.com/Lestropie/IP-freely/issues/5\r\n\n\n### Communication channels\n\nTBA\n\n### Skills\n\n-   Python: Moderate\r\n\r\n    The code logic for manipulating metadata will necessitate some competence with Python dictionaries; nothing super complex, but maybe not accessible for someone who has never touched them.\r\n    Expect to make use of the `pathlib` module.\r\n    If any contributor were to have existing expertise with `pybids` that may also be beneficial.\r\n\r\n-   BIDS: Variable\r\n\r\n    The necessary fundamentals of BIDS are just filesystem structure (directories, entities and suffices) and the idea of a metadata dictionary.\r\n    However creation of exemplar datasets would be facilitated by someone who:\r\n    -   Has experience with BIDS across multiple modalities\r\n    -   Has some familiarity with the Inheritance Principle.\r\n\n\n### Onboarding documentation\n\nCurrent status of the Inheritance Principle:\r\nhttps://bids-specification.readthedocs.io/en/stable/common-principles.html#the-inheritance-principle\r\n\r\nOriginal context that motivated pursuit of augmentation of the Inheritance Principle:\r\nhttps://github.com/bids-standard/bids-bep016/issues/50\r\n\r\nPreviously proposed (but rejected) extension of the Inheritance Principle:\r\nhttps://github.com/bids-standard/bids-specification/pull/1003\r\n(and other threads linked therein)\r\n\r\nExisting repository that contains data-empty exemplar datasets for the purpose of validation:\r\nhttps://github.com/bids-standard/bids-examples\r\n\r\nDiscussion regarding potential modification of Inheritance Principle for BIDS 2.0:\r\nhttps://github.com/bids-standard/bids-2-devel/issues/65\r\n\n\n### What will participants learn?\n\n-   Experience building a piece of open source scientific software from scratch\r\n\r\n-   Basic algorithmic design for the various manipulations of metadata\r\n\r\n-   Understanding correspondence between specification rules as described in plaintext language and programmatic implementation\r\n\r\n-   Can provide an introduction to the basics of Git for any participants not already familiar with such.\r\n\n\n### Data to use\n\nProper evaluation of the proposed tool will necessitate construction of one or more novel datasets.\r\n\r\nSome insight may be gained from executing the tool against any existing BIDS datasets, whether public or private. Of particular interest would be any datasets known to already be utilising the Inheritance Principle.\r\n\n\n### Number of collaborators\n\n1\n\n### Credit to collaborators\n\nIntend to set up the GitHub all-contributors bot for this new Project.\r\n\r\nDepending on scope and eventual adoption, publication in the Journal of Open Source Science (JOSS) may be pursued.\r\n\n\n### Image\n\nLeave this text if you don't have an image yet.\n\n### Type\n\ncoding_methods, data_management\n\n### Development status\n\n0_concept_no_content\n\n### Topic\n\nreproducible_scientific_methods\n\n### Tools\n\nBIDS\n\n### Programming language\n\nPython\n\n### Modalities\n\nbehavioral, DWI, ECG, ECOG, EEG, eye_tracking, fMRI, fNIRS, MEG, MRI, PET, TDCS, TMS\n\n### Git skills\n\n0_no_git_skills\n\n### Anything else?\n\n_No response_\n\n### Things to do after the project is submitted and ready to review.\n\n- [ ] Add a comment below the main post of your issue saying: `Hi @brainhackorg/project-monitors my project is ready!`\n- [x] Twitter-sized summary of your project pitch.",
  "project_url": "https://github.com/Lestropie/IP-freely",
  "project_description": "\n\nThe Inheritance Principle (\"IP\") has been a feature of the Brain Imaging Data Structure (BIDS) since its inception. It describes how the metadata relevant to one specific data file may in fact originate from multiple metadata files. Encoding some common metadata field just once, and having it be deemed applicable to multiple metadata files, may both reduce redundancy and communicate the intrinsic hierarchical structure of the dataset. This however comes at considerable complexity to the specification itself and the software responsible for interfacing with such data. Indeed nearly a decade after its creation, many software APIs for parsing BIDS data still do not support the Inheritance Principle.\r\n\r\nThe future of the IP is at a crossroads, particularly as work progresses toward BIDS 2.0:\r\n-   On one hand, some would like for the IP to disappear entirely: all metadata relevant to any given data file would need to be stored in a sidecar metadata file alongside that data file, regardless of duplication.\r\n-   On the other, not just preserving the IP but *augmenting* it could better communicate the complex hierarchical dependencies of complex datasets, particularly derivative data.\r\n\r\nThe goals of this project are twofold.\r\n\r\n1.  There is a dearth of existing software tools for managing the IP. If a dataset that exploits the IP were provided as input to a BIDS App that is naive to the IP, that App could perform improper association of metadata. Existing datasets may contain substantial metadata redundancy, due to not currently having an easy way through which to exploit the IP. A tool to automate such data manipulations could therefore be useful in the BIDS ecosystem.\r\n\r\n2.  Consequential decisions regarding the IP and related issues in BIDS 2.0 would be better informed if stakeholders could see the effects that proposed specifications would have on how compliant datasets appear.\r\n\n\n"
}