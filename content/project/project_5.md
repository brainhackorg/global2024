{
  "Title": "behapy: A behavioural neuroscience analysis package for Python",
  "link_to_issue": "https://github.com/brainhackorg/global2024/issues/5",
  "issue_number": 5,
  "labels": [
    {
      "name": "git_skills:1_commit_push",
      "description": "",
      "color": "5B6C2C"
    },
    {
      "name": "hub:melbourne_aus",
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
      "name": "project_type:pipeline_development",
      "description": null,
      "color": "ededed"
    },
    {
      "name": "project_type:visualisation",
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
      "name": "topic:data_visualisation",
      "description": "",
      "color": "FBCA04"
    },
    {
      "name": "topic:systems_neuroscience",
      "description": "",
      "color": "FBCA04"
    }
  ],
  "content": "### Title\n\nbehapy: A behavioural neuroscience analysis package for Python\n\n### Leaders\n\nChris Nolan\n\n### Collaborators\n\n_No response_\n\n### Brainhack Global 2024 Event\n\nBrainhack Aus\n\n### Project Description\n\nStudies using optic fibres to record real-time fluorescent biosensors in-vivo are now commonplace, yet despite an increasing literature on best practices for analysing such data, there is a surprising lack of fit-for-purpose API-level tooling. This project is a continuing effort to fill this gap by providing flexible Python-based implementations of common normalisation and artefact correction procedures for fluorescent biosensors, along with useful event-based analyses.\r\n\r\nThe goals of this project will extend beyond Brainhack Global 2024, but all are in an effort to create an open-source API and workbench for analysing fibre photometry data in a behavioural neuroscience context. Since Brainhack Global 2022, we have created a basic artefact-rejection workbench, a preprocessing stage and implemented simple linear regression for event-level analysis. This year the goal is to create a method to benchmark normalisation methods by creating data simulation functionality under different assumptions about the sources of recording noise. We are also aiming to generalise second-level linear mixed model testing for events of interest.\n\n### Link to project repository/sources\n\nhttps://github.com/crnolan/behapy\n\n### Goals for Brainhack Global\n\n* Create a utility for simulating raw fibre photometry data under a variety of assumptions (for testing the toolkit).\r\n* Implement second-level linear mixed model tests for events of interest.\r\n* Develop both API-level and tutorial documentation. Docstrings are currently sparse and light on detail, and walkthroughs are virtually non-existent.\r\n* Add import scripts for MedPC datasets, and put together a skeleton framework for event summary and plotting functions.\n\n### Good first issues\n\n1. Check and update installation instructions for behapy package.\r\n2. Document end-user experience for running existing fibre preprocessing workbench on sample data.\r\n3. Establish a configuration format / tool for importing structured MedPC files.\r\n4. Add the capability in the pre-processing interface to interactively compare / select different but reasonable normalisation methods.\n\n### Communication channels\n\nhttps://mattermost.brainhack.org/brainhack/channels/behapy\n\n### Skills\n\nPrimarily, some knowledge of fluorescent biosensor normalisation and analysis procedures will be useful. We'll be predominantly working in Python, but there will be tasks for all levels of Python competency.\r\n\r\nBonus useful skills:\r\n\r\n* Signal processing (we'll be filtering and fitting timeseries data)\r\n* Python interactive visualisation (bokeh / holoviews / panel / seaborn / matplotlib)\r\n* Working knowledge of linear regression and mixed effects models\r\n* BIDS experience - while we won't be attempting to add an official BIDS extension for fibre photometry in this project, we are trying to stay approximately in line with BIDS format\n\n### Onboarding documentation\n\n_No response_\n\n### What will participants learn?\n\n* Data manipulation in Python (numpy / pandas)\r\n* Signal filtering in Python\r\n* GitHub collaboration techniques\n\n### Data to use\n\nBYO fibre & behavioural data - we'll create a repository of useful examples.\n\n### Number of collaborators\n\n3\n\n### Credit to collaborators\n\nProject contributors will be listed on the project README (hosted on github).\n\n### Image\n\nLeave this text if you don't have an image yet.\n\n### Type\n\ndata_management, pipeline_development, visualization\n\n### Development status\n\n0_concept_no_content\n\n### Topic\n\ndata_visualisation, systems_neuroscience\n\n### Tools\n\nBIDS, other\n\n### Programming language\n\nPython\n\n### Modalities\n\nbehavioral, other\n\n### Git skills\n\n1_commit_push\n\n### Anything else?\n\n_No response_\n\n### Things to do after the project is submitted and ready to review.\n\n- [x] Add a comment below the main post of your issue saying: `Hi @brainhackorg/project-monitors my project is ready!`\n- [ ] Twitter-sized summary of your project pitch.",
  "project_url": "https://github.com/crnolan/behapy",
  "project_description": "\n\nStudies using optic fibres to record real-time fluorescent biosensors in-vivo are now commonplace, yet despite an increasing literature on best practices for analysing such data, there is a surprising lack of fit-for-purpose API-level tooling. This project is a continuing effort to fill this gap by providing flexible Python-based implementations of common normalisation and artefact correction procedures for fluorescent biosensors, along with useful event-based analyses.\r\n\r\nThe goals of this project will extend beyond Brainhack Global 2024, but all are in an effort to create an open-source API and workbench for analysing fibre photometry data in a behavioural neuroscience context. Since Brainhack Global 2022, we have created a basic artefact-rejection workbench, a preprocessing stage and implemented simple linear regression for event-level analysis. This year the goal is to create a method to benchmark normalisation methods by creating data simulation functionality under different assumptions about the sources of recording noise. We are also aiming to generalise second-level linear mixed model testing for events of interest.\n\n"
}