{
  "Title": "EEL-Hack: Learning to develop an mTRF pipeline with eelbrain",
  "link_to_issue": "https://github.com/brainhackorg/global2024/issues/19",
  "issue_number": 19,
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
      "name": "modality:EEG",
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
      "name": "project_development_status:1_basic structure",
      "description": "",
      "color": "D93F0B"
    },
    {
      "name": "project_type:documentation",
      "description": null,
      "color": "ededed"
    },
    {
      "name": "project_type:pipeline_development",
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
      "name": "tools:MNE",
      "description": "",
      "color": "EA1D4E"
    },
    {
      "name": "topic:neural_encoding",
      "description": null,
      "color": "ededed"
    }
  ],
  "content": "### Title\r\n\r\nEEL-Hack: Learning to develop an mTRF pipeline with eelbrain\r\n\r\n### Leaders\r\n\r\nNoemi Bonfiglio\r\nVincenzo Verbeni\r\n\r\n### Collaborators\r\n\r\nNan\r\n\r\n### Brainhack Global 2024 Event\r\n\r\nBrainhack Donostia\r\n\r\n### Project Description\r\n\r\nThe Multivariate Temporal Response Function (mTRF) method is an advanced technique used to model the relationship between various features of an auditory stimulus\u2014such as acoustic (e.g., sound envelope) and lexical (e.g., word boundaries, semantic information) features\u2014and the brain's electrical activity as measured by M/EEG signals. This approach provides insights into how the brain processes auditory information over time, enabling researchers to link neural dynamics with complex auditory inputs.\r\nIn this project, we will walk through the process of analyzing EEG data using the mTRF method, leveraging the Python toolbox Eelbrain to manage data, prepare predictors, and analyze results. The main steps involved in this project will be:\r\n\r\n**1. Converting Data Structure from BIDS to Eelbrain Format**\r\n\r\nThe BIDS format is a standardized organization of M/EEG datasets, but Eelbrain uses a different structure for managing and analyzing data. Therefore, we will organize the data according to Eelbrain\u2019s requirements. \r\n\r\n**2. Defining the Experiment Design**\r\n\r\nOnce the data has been converted, the next step is to define the experiment design. This involves inspecting the events recorded in the EEG data, which mark key moments such as stimulus presentation or participant responses, and ensuring they are correctly aligned with the corresponding auditory stimuli. This step is crucial because accurate event marking is essential for relating the brain signals to specific time points in the stimuli. \r\n\r\n**3. Building an experiment.py Script According to the Design**\r\n\r\nWith the experiment design in place, we will implement the design in a Python script, experiment.py, which automates the process of loading and organizing the data for analysis. This script will:\r\nLoad the EEG data and events from the converted Eelbrain format.\r\nLoad the corresponding stimuli features (e.g., sound waveforms, lexical properties).\r\nSynchronize the EEG recordings with the stimuli based on the experiment design.\r\n\r\n**4. Preparing the Predictors (e.g., Gammatones)**\r\n\r\nBefore fitting the mTRF model, we need to prepare the predictors that will be used to relate the brain\u2019s response to the auditory stimuli. Predictors can include a variety of acoustic and lexical features. Our main goal will be to prepare acoustic predictors for our mTRFs. Optionally, depending on the time available during BrainHack, we will work on lexical predictors - such as word frequency and surprisal.\r\n\r\n**5. Fitting an mTRF at the Group Level and plotting the results**\r\n\r\nOnce the data and predictors are prepared, we will fit the mTRF model at the group level to investigate how different stimulus features are encoded in the brain\u2019s neural activity over time. We will then inspect the results plotting the mTRF coefficients over time and the  topographical maps showing the variations of these coefficients across different regions of the scalp.\r\n\r\n\r\n\r\n### Link to project repository/sources\r\n\r\nNaN\r\n\r\n### Goals for Brainhack Global\r\n\r\na) understanding how mTRF method works\r\nb) understanding how Eeelbrain works\r\nc) writing and editing scripts to prepare the data and fit an mTRFs\r\n\r\n\r\n### Good first issues\r\n\r\nissue 1: converting data structure from bids to Eelbrain format\r\nissue 2: define the experiment design (i.e., checking events in the eeg data and the corresponding stimuli)\r\nissue 3: building an experiment.py script according to the design \r\nissue 3: prepare the predictors (e.g., gammatones)\r\nissue 4: fit an mTRF at the group level\r\nissue 5: plotting the mTRF results\r\n\r\n\r\n\r\n### Communication channels\r\n\r\nNaN\r\n\r\n### Skills\r\n\r\n- basic python skills\r\n- basic knowledge of electrophysiological data\r\n\r\n\r\n### Onboarding documentation\r\n\r\nNaN\r\n\r\n### What will participants learn?\r\n\r\nHow to use Eelbrain\r\n\r\n### Data to use\r\n\r\nThe following is a link to the EEG dataset (published in BIDS format on OSF) that we will use for our project:\r\n\r\nhttps://osf.io/xq263/\r\n\r\n### Number of collaborators\r\n\r\n2\r\n\r\n### Credit to collaborators\r\n\r\nProject contributors will be listed in the project's README.\r\n\r\n### Image\r\n\r\nLeave this text if you don't have an image yet.\r\n\r\n### Type\r\n\r\npipeline_development\r\n\r\n### Development status\r\n\r\n1_basic structure\r\n\r\n### Topic\r\n\r\nneural_encoding\r\n\r\n### Tools\r\n\r\nMNE\r\n\r\n### Programming language\r\n\r\nPython\r\n\r\n### Modalities\r\n\r\nEEG\r\n\r\n### Git skills\r\n\r\n0_no_git_skills\r\n\r\n### Anything else?\r\n\r\n_No response_\r\n\r\n### Things to do after the project is submitted and ready to review.\r\n\r\n- [X] Add a comment below the main post of your issue saying: `Hi @brainhackorg/project-monitors my project is ready!`\r\n- [X] Twitter-sized summary of your project pitch.",
  "project_description": "\r\n\r\nThe Multivariate Temporal Response Function (mTRF) method is an advanced technique used to model the relationship between various features of an auditory stimulus\u2014such as acoustic (e.g., sound envelope) and lexical (e.g., word boundaries, semantic information) features\u2014and the brain's electrical activity as measured by M/EEG signals. This approach provides insights into how the brain processes auditory information over time, enabling researchers to link neural dynamics with complex auditory inputs.\r\nIn this project, we will walk through the process of analyzing EEG data using the mTRF method, leveraging the Python toolbox Eelbrain to manage data, prepare predictors, and analyze results. The main steps involved in this project will be:\r\n\r\n**1. Converting Data Structure from BIDS to Eelbrain Format**\r\n\r\nThe BIDS format is a standardized organization of M/EEG datasets, but Eelbrain uses a different structure for managing and analyzing data. Therefore, we will organize the data according to Eelbrain\u2019s requirements. \r\n\r\n**2. Defining the Experiment Design**\r\n\r\nOnce the data has been converted, the next step is to define the experiment design. This involves inspecting the events recorded in the EEG data, which mark key moments such as stimulus presentation or participant responses, and ensuring they are correctly aligned with the corresponding auditory stimuli. This step is crucial because accurate event marking is essential for relating the brain signals to specific time points in the stimuli. \r\n\r\n**3. Building an experiment.py Script According to the Design**\r\n\r\nWith the experiment design in place, we will implement the design in a Python script, experiment.py, which automates the process of loading and organizing the data for analysis. This script will:\r\nLoad the EEG data and events from the converted Eelbrain format.\r\nLoad the corresponding stimuli features (e.g., sound waveforms, lexical properties).\r\nSynchronize the EEG recordings with the stimuli based on the experiment design.\r\n\r\n**4. Preparing the Predictors (e.g., Gammatones)**\r\n\r\nBefore fitting the mTRF model, we need to prepare the predictors that will be used to relate the brain\u2019s response to the auditory stimuli. Predictors can include a variety of acoustic and lexical features. Our main goal will be to prepare acoustic predictors for our mTRFs. Optionally, depending on the time available during BrainHack, we will work on lexical predictors - such as word frequency and surprisal.\r\n\r\n**5. Fitting an mTRF at the Group Level and plotting the results**\r\n\r\nOnce the data and predictors are prepared, we will fit the mTRF model at the group level to investigate how different stimulus features are encoded in the brain\u2019s neural activity over time. We will then inspect the results plotting the mTRF coefficients over time and the  topographical maps showing the variations of these coefficients across different regions of the scalp.\r\n\r\n\r\n\r\n"
}