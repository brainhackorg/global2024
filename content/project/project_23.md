{
  "Title": "Bayes and Bach: An RNN-powered affair",
  "link_to_issue": "https://github.com/brainhackorg/global2024/issues/23",
  "issue_number": 23,
  "labels": [
    {
      "name": "git_skills:0_none",
      "description": "",
      "color": "5B6C2C"
    },
    {
      "name": "hub:donostia_esp",
      "description": "",
      "color": "0E8A16"
    },
    {
      "name": "modality:behavioral",
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
      "name": "project_type:documentation",
      "description": null,
      "color": "ededed"
    },
    {
      "name": "project_type:method_development",
      "description": null,
      "color": "ededed"
    },
    {
      "name": "status:web_ready",
      "description": "",
      "color": "0E8A16"
    },
    {
      "name": "topic:machine_learning",
      "description": "",
      "color": "FBCA04"
    }
  ],
  "content": "### Title\n\nBayes and Bach: An RNN-powered affair\n\n### Leaders\n\nAlejandro Tabas (mattermost: @atabas) \n\n### Collaborators\n\n_No response_\n\n### Brainhack Global 2024 Event\n\nBrainhack Donostia\n\n### Project Description\n\nWe want to do a proof-of-concept: test whether artificial recurrent neural networks (RNN) learn to predict the next tone when trying to perceive music in a noisy environment.\r\n\r\nThis is an accessible project that does not require an extensive coding expertise. Participants that want to contribute with coding will be recommended to do this in python, although data retrieval can be done in any other language. Participants who do not wish to contribute with code can contribute either with a) their musical expertise in Data Preprocessing and during the interpretation of the Testing, or b) their patience and web-browsing skills to manual data retrieval.\r\n\r\nWe will start by collecting a lot of Bach's compositions. We will transform each composition into a sequence of tokens: each token will be one note or several notes (i.e., a chord) that were meant to be played together in the original composition. For this proof-of-concept we will ignore information about the duration or loudness of each note/chord. For each sequence, we will generate two items: a ground-truth (the sequence itself), and a set of observations (the sequence plus some noise that will corrupt part of the information).\r\n\r\nWe will then present the observations to the RNN and train its weights so that, for each of the observation sequences, the RNN is able to extract the ground-truth sequence. In other words: we will train the RNNs to perceive the original musical sequence usign only the noisy observations.\r\n\r\nAfter the training we will test whether the RNN is encoding, in its internal states, a set of predictions on the next token. If that is the case, we will conclude that the RNN is actively attempting to predict the next item to implement perception.\r\n\r\nThe results will help us generating hypotheses on how the brain decodes music. The neuroscientific community will be able to use these hypotheses to inform the design of experiments IRL brains.\r\n\r\nMore details and resources in the github repository\n\n### Link to project repository/sources\n\nhttps://github.com/qtabs/BayesPlusBach/\r\nhttps://mattermost.brainhack.org/brainhack/channels/bh-donostia-2024--bayes-3-bach\n\n### Goals for Brainhack Global\n\nMilestones:\r\n- A web scrapper that collects MIDI files of Bach's compositions\r\n- A collection of MIDI files of Bach's compositions\r\n- A MIDI-to-data pipeline that transforms MIDI files in pairs of (ground-truth, observation) that can be used for training\r\n- Several RNN architectures designed to retrieve the ground truth from noisy observations of sequences of tones/chords\r\n- The trained RNN(s)\r\n- Validation/refutation of the starting hypothesis\n\n### Good first issues\n\n1. Automatise the retrieval of Bach's MIDIs \r\n2. Automatise the encoding of a MIDI into a training sample for the RNN\r\n3. Build an RNN architecture to predict the training samples.\r\n\n\n### Communication channels\n\nhttps://mattermost.brainhack.org/brainhack/channels/bh-donostia-2024--bayes-3-bach\n\n### Skills\n\nPython: all levels\n\n### Onboarding documentation\n\nhttps://github.com/qtabs/BayesPlusBach/blob/main/CONTRIBUTING.md\n\n### What will participants learn?\n\nWeb scrapping with python\r\nTraining RNNs with pytorch\n\n### Data to use\n\nResources on MIDI files: [This website](http://www.jsbach.net/midi/index.html) could be a good place to start. [This other website](http://www.jsbach.net/bcs/link-midi.html) has a lot of links with potentially better quality MIDI files. The better the quality of the MIDI, the easier the work of the preprocesser(s)!\r\n\r\nResources on data scrappers: I used [this tutorial](https://www.geeksforgeeks.org/python-web-scraping-tutorial/) when I needed to implemet a scraper in the past. This [other tutorial](https://realpython.com/python-web-scraping-practical-introduction/) also looks informative and easy to follow.\n\n### Number of collaborators\n\n3\n\n### Credit to collaborators\n\nContributors will be listed in the contributors textfile.\n\n### Image\n\n![00017-3587716162](https://github.com/user-attachments/assets/bda03b4a-df64-4aee-bb91-c2faa7765e35)\r\n\n\n### Type\n\nmethod_development\n\n### Development status\n\n0_concept_no_content\n\n### Topic\n\nmachine_learning\n\n### Tools\n\nother\n\n### Programming language\n\nPython\n\n### Modalities\n\nbehavioral\n\n### Git skills\n\n0_no_git_skills\n\n### Anything else?\n\n_No response_\n\n### Things to do after the project is submitted and ready to review.\n\n- [ ] Add a comment below the main post of your issue saying: `Hi @brainhackorg/project-monitors my project is ready!`\n- [ ] Twitter-sized summary of your project pitch.",
  "project_url": "https://github.com/qtabs/BayesPlusBach/https://mattermost.brainhack.org/brainhack/channels/bh-donostia-2024--bayes-3-bach",
  "project_description": "\n\nWe want to do a proof-of-concept: test whether artificial recurrent neural networks (RNN) learn to predict the next tone when trying to perceive music in a noisy environment.\r\n\r\nThis is an accessible project that does not require an extensive coding expertise. Participants that want to contribute with coding will be recommended to do this in python, although data retrieval can be done in any other language. Participants who do not wish to contribute with code can contribute either with a) their musical expertise in Data Preprocessing and during the interpretation of the Testing, or b) their patience and web-browsing skills to manual data retrieval.\r\n\r\nWe will start by collecting a lot of Bach's compositions. We will transform each composition into a sequence of tokens: each token will be one note or several notes (i.e., a chord) that were meant to be played together in the original composition. For this proof-of-concept we will ignore information about the duration or loudness of each note/chord. For each sequence, we will generate two items: a ground-truth (the sequence itself), and a set of observations (the sequence plus some noise that will corrupt part of the information).\r\n\r\nWe will then present the observations to the RNN and train its weights so that, for each of the observation sequences, the RNN is able to extract the ground-truth sequence. In other words: we will train the RNNs to perceive the original musical sequence usign only the noisy observations.\r\n\r\nAfter the training we will test whether the RNN is encoding, in its internal states, a set of predictions on the next token. If that is the case, we will conclude that the RNN is actively attempting to predict the next item to implement perception.\r\n\r\nThe results will help us generating hypotheses on how the brain decodes music. The neuroscientific community will be able to use these hypotheses to inform the design of experiments IRL brains.\r\n\r\nMore details and resources in the github repository\n\n"
}