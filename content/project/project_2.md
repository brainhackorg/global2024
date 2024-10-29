{
  "Title": "MRI denoising using MP-PCA",
  "link_to_issue": "https://github.com/brainhackorg/global2024/issues/2",
  "issue_number": 2,
  "labels": [
    {
      "name": "git_skills:1_commit_push",
      "description": "",
      "color": "5B6C2C"
    },
    {
      "name": "hub:australasia_aus",
      "description": "",
      "color": "0E8A16"
    },
    {
      "name": "modality:DWI",
      "description": "",
      "color": "1d76db"
    },
    {
      "name": "modality:fMRI",
      "description": "",
      "color": "1d76db"
    },
    {
      "name": "modality:MRI",
      "description": "",
      "color": "1d76db"
    },
    {
      "name": "programming:C++",
      "description": "",
      "color": "5319E7"
    },
    {
      "name": "programming:documentation",
      "description": "",
      "color": "5319E7"
    },
    {
      "name": "project",
      "description": "",
      "color": "B60205"
    },
    {
      "name": "project_development_status:2_releases_existing",
      "description": "",
      "color": "D93F0B"
    },
    {
      "name": "project_type:coding_methods",
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
      "name": "tools:MRtrix",
      "description": "",
      "color": "EA1D4E"
    },
    {
      "name": "topic:PCA",
      "description": "",
      "color": "FBCA04"
    },
    {
      "name": "topic:diffusion",
      "description": null,
      "color": "ededed"
    }
  ],
  "content": "### Title\n\nImproving MP-PCA denoising of diffusion and functional MRI data using MP-PCA\n\n### Leaders\n\nRobert E. Smith; http://x.com/Lestropie\n\n### Collaborators\n\n_No response_\n\n### Brainhack Global 2024 Event\n\nBrainhack Aus\n\n### Project Description\n\nDenoising of EPI MRI data has become a common component of MRI pre-processing pipelines. It is most prevalent in the pre-processing of diffusion MRI data given its low signal magnitude, but it is also becoming increasingly prevalent for functional MRI pre-processing.\r\n\r\nThe *MRtrix3* software provides a command `dwidenoise` for this purpose. This is a sliding-window approach, where processing for each voxel is performed based on data in a local spatial neighbourhood, exploiting the density of EPI data across multiple volumes. After performing a Principal Component Analysis (PCA) decomposition for the data across DWI volumes within that window, it determines the appropriate cutoff for which components to retain vs. remove based on the Marchenko-Pastur distribution, which predicts the distribution of eigenvalues for random matrices. By doing so it intends to retain the useful signal present in that location, but remove those components that manifest from the thermal noise of the imaging process.\r\n\r\nWhile currently in wide use, there are many prospective enhancements that could be made to this command to improve the quality of denoising. The goal of this project is to address features with strong prospects for improving performance that are achievable within the short time frame of a Hackathon.\r\n\n\n### Link to project repository/sources\n\n`dwidenoise` enhancements meta-issue: https://github.com/MRtrix3/mrtrix3/issues/3023\r\n\n\n### Goals for Brainhack Global\n\n-   Primary goal: Spherical kernel\r\n\r\n    Give the command the ability to use a spherically-shaped sliding window kernel as an alternative to the current cubic kernel.\r\n\r\n-   Primary goal: Noise level as input/output\r\n\r\n    Currently, the command receives as input a DWI series, produces as output a denoised DWI series, and may optionally export the estimated noise level. Would like to change this in two ways. Firstly, it should be possible to just export the estimated noise level, withholding the output DWI series. Secondly, it should be possible to take as input an estimated noise level, and denoise the input DWI series based on that pre-estimated noise level. Doing this would allow for the filtering of that noise level estimate, potentially addressing errors in the otherwise independent-per-voxel noise level estimation.\r\n\r\n-   Secondary goals: Any other items in https://github.com/MRtrix3/mrtrix3/issues/3023 that may be of interest to a participant.\n\n### Good first issues\n\nThis Project is only intended for potential contributors who already possess strong software engineering skills.\n\n### Communication channels\n\nTBA\n\n### Skills\n\n-   C++: requisite\r\n    As the existing `dwidenoise` command is written in C++, and the *MRtrix3* API uses advanced C++ features, existing competence with this language is a prerequisite for this Project.\r\n\r\n-   Diffusion MRI: optional\r\n    While not strictly necessary, it may be beneficial to have some experience / interest in diffusion MRI to take on this task. I will however note that some of the planned improvements to `dwidenoise` actually primarily have its application to functional MRI denoising in mind.\r\n\r\n-   PCA: optional\r\n    Not strictly necessary, but some baseline knowledge of what PCA is / does would be beneficial.\n\n### Onboarding documentation\n\n*MRtrix3* contributing documentation: https://github.com/MRtrix3/mrtrix3/blob/master/CONTRIBUTING.md\r\n\r\nNote that these developments would be targeted at the \"`dev`\" development branch of *MRtrix3*. This branch has undergone substantial changes to the build system. Therefore, even if an attendee has had prior experience building *MRtrix3* from source, it will be necessary to have or build some experience with `cmake`.\r\n\r\nMP-PCA method journal article: https://www.sciencedirect.com/science/article/pii/S1053811916303949\r\n\n\n### What will participants learn?\n\n-   Real-world application of advanced C++, including templating\r\n-   Gain experience with the *MRtrix3* C++ API, which may be useful for other image processing development projects\r\n-   Experience with PCA and the issues of rank selection\n\n### Data to use\n\nI will endeavour to obtain some different example data that can be used for testing. It is also common to hear complaints about inefficacy of DWI denoising, in which case it would be beneficial to obtain sample datasets from the community. Attendees may also bring their own data and see the consequences of technical enhancements to denoising performance.\n\n### Number of collaborators\n\n1\n\n### Credit to collaborators\n\nOnce commits are merged to `master` as part of a tagged release, contributors appear at the tail of the *MRtrix3* website [front page](http://mrtrix.org), and will receive attribution for their specific contributions as part of a changelog ([see example](https://community.mrtrix.org/t/mrtrix-3-0-4-release/6263)).\n\n### Image\n\nLeave this text if you don't have an image yet.\n\n### Type\n\ncoding_methods, method_development\n\n### Development status\n\n2_releases_existing\n\n### Topic\n\ndiffusion, PCA\n\n### Tools\n\nMRtrix\n\n### Programming language\n\nC++\n\n### Modalities\n\nDWI, fMRI\n\n### Git skills\n\n1_commit_push\n\n### Anything else?\n\nThis project has a much higher barrier to entry than most Hackathon projects. It will only proceed if there exists in attendance at least one other participant with both sufficient interest in the project and competence with C++.\n\n### Things to do after the project is submitted and ready to review.\n\n- [ ] Add a comment below the main post of your issue saying: `Hi @brainhackorg/project-monitors my project is ready!`\n- [ ] Twitter-sized summary of your project pitch.",
  "project_url": "https://github.com/MRtrix3/mrtrix3/issues/3023",
  "project_description": "\n\nDenoising of EPI MRI data has become a common component of MRI pre-processing pipelines. It is most prevalent in the pre-processing of diffusion MRI data given its low signal magnitude, but it is also becoming increasingly prevalent for functional MRI pre-processing.\r\n\r\nThe *MRtrix3* software provides a command `dwidenoise` for this purpose. This is a sliding-window approach, where processing for each voxel is performed based on data in a local spatial neighbourhood, exploiting the density of EPI data across multiple volumes. After performing a Principal Component Analysis (PCA) decomposition for the data across DWI volumes within that window, it determines the appropriate cutoff for which components to retain vs. remove based on the Marchenko-Pastur distribution, which predicts the distribution of eigenvalues for random matrices. By doing so it intends to retain the useful signal present in that location, but remove those components that manifest from the thermal noise of the imaging process.\r\n\r\nWhile currently in wide use, there are many prospective enhancements that could be made to this command to improve the quality of denoising. The goal of this project is to address features with strong prospects for improving performance that are achievable within the short time frame of a Hackathon.\r\n\n\n"
}