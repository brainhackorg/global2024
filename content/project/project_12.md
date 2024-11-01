{
  "Title": "PsyR: An R package for better inference in multivariate statistical analysis",
  "link_to_issue": "https://github.com/brainhackorg/global2024/issues/12",
  "issue_number": 12,
  "labels": [
    {
      "name": "git_skills:1_commit_push",
      "description": "",
      "color": "5B6C2C"
    },
    {
      "name": "git_skills:2_branches_PRs",
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
      "name": "modality:eye_tracking",
      "description": "",
      "color": "1d76db"
    },
    {
      "name": "programming:documentation",
      "description": "",
      "color": "5319E7"
    },
    {
      "name": "programming:R",
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
      "name": "project_tools_skills:comfortable",
      "description": null,
      "color": "ededed"
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
      "name": "topic:statistical_modelling",
      "description": "",
      "color": "FBCA04"
    }
  ],
  "content": "### Title\r\n\r\nPsyR: An R package for better inference in multivariate statistical analysis\r\n\r\n### Leaders\r\n\r\nKelly Garner (Mattermost: kels)\r\n\r\n\r\n\r\n### Collaborators\r\n\r\nChristopher Nolan (Mattermost: cnolan)\r\n\r\n### Brainhack Global 2024 Event\r\n\r\nBrainhack Aus\r\n\r\n### Project Description\r\n\r\nWe consistently use massive data sets across neuroscience and psychology. The routine gathering of big data requires that we are well equipped with tools that allow us to conduct appropriate multivariate statistics.\r\n\r\nMultivariate statistical analysis typically follows a two stage procedure, an omnibus test of the global null hypothesis followed by post-hoc tests of specific effects. It is not well known that under certain circumstances this leads to a drastically inflated rate of type 1 error. It is even less well known that this procedure can also lead to an even lessor known type IV error (incorrect interpretation of a correctly rejected hypothesis)!\r\n\r\nIt is possible to avoid these dragons by using an alternative procedure where all inferences are derived from simultaneous confidence intervals (SCIs) on contrasts of interest. This approach provides interval inferences on effect sizes and it also ensures that the familywise type 1 error rate associated with directional inferences (the inferences usually derived from tests of null hypotheses) is controlled at alpha. One piece of software (PSY) can produce SCIs appropriate for planned analyses (where contrasts are defined independently of the data) and for more flexible analyses where contrasts are defined on a post hoc basis. However, this software is only available for use on windows and cannot be scripted into reproducible workflows.\r\n\r\nWe have been building an R package that implements the functions of PSY, and to make this method of statistical inference available to the masses! We are ready for you to play with some of the functions to analyse your own data, and create Quarto documents that document your workflow, to help future users. If you are feeling hacky enough, we could also use help developing further the R package, which is around 80% finished right now.\r\n\r\n\r\n\r\n### Link to project repository/sources\r\n\r\nhttps://github.com/kel-github/PSY2R - this has all the code we used to get started. I'll share the package code at the event\r\nhttps://doi.org/10.1177/0013164402062002001 - this is the paper that defines the functionality of Psy.\r\nhttps://r-pkgs.org/ - Hadley Wickham's bible for building R packages\r\n\r\n### Goals for Brainhack Global\r\n\r\nBring your own data and use the functions we have already written. This will help us learn how user friendly they are and what can be done to improve interaction with the function.\r\nDocument own data analysis in quarto documents to help future users\r\nContribute to the R package, particularly with higher level functions that handle data wrangling and standardisation\r\nBuild a GitHub website for the package\r\n\r\n### Good first issues\r\n\r\n1. issue one: read [this paper](https://doi.org/10.1177/0013164402062002001 to get an overview of what Psy does)\r\n\r\n2. issue two: find a dataset that requires an ANOVA analysis, share it with the team and we'll talk you through how to use Psy to analyse it\r\n\r\n3. issue three: If not already, get comfortable with quarto documents - https://quarto.org/ \r\n\r\n4. issue four: Go through the exercises that show you how to create an R package in [chapter 1 of this book](https://r-pkgs.org/whole-game.html).\r\n\r\n\r\n### Communication channels\r\n\r\nhttps://mattermost.brainhack.org/brainhack/channels/psy2r\r\n\r\n### Skills\r\n\r\n- R: basic and advanced\r\n- Stats knowledge: can run an ANOVA and know what a confidence interval is\r\n- Github: can clone and make pull requests (if needed, we'll show you how)\r\n\r\n### Onboarding documentation\r\n\r\n_No response_\r\n\r\n### What will participants learn?\r\n\r\nParticipants will learn about multivariate data analysis: \r\n- how to compute confidence intervals for between x within effects, ideally on their own data\r\n- what goes under the hood of an R package\r\n\r\n### Data to use\r\n\r\n_No response_\r\n\r\n### Number of collaborators\r\n\r\n4\r\n\r\n### Credit to collaborators\r\n\r\nProject contributors will be listed in the project ReadMe, and as authors on any help documents\r\n\r\n### Image\r\n\r\nLeave this text if you don't have an image yet.\r\n\r\n### Type\r\n\r\ncoding_methods, documentation, pipeline_development\r\n\r\n### Development status\r\n\r\n1_basic structure\r\n\r\n### Topic\r\n\r\nstatistical_modelling\r\n\r\n### Tools\r\n\r\nother\r\n\r\n### Programming language\r\n\r\n`R`\r\n\r\n### Modalities\r\n\r\nbehavioral, eye_tracking\r\n\r\n### Git skills\r\n\r\n1_commit_push, 2_branches_PRs\r\n\r\n### Anything else?\r\n\r\n_No response_\r\n\r\n### Things to do after the project is submitted and ready to review.\r\n\r\n- [X] Add a comment below the main post of your issue saying: `Hi @brainhackorg/project-monitors my project is ready!`\r\n- [X] Twitter-sized summary of your project pitch.",
  "project_url": "https://github.com/kel-github/PSY2R",
  "project_description": "\r\n\r\nWe consistently use massive data sets across neuroscience and psychology. The routine gathering of big data requires that we are well equipped with tools that allow us to conduct appropriate multivariate statistics.\r\n\r\nMultivariate statistical analysis typically follows a two stage procedure, an omnibus test of the global null hypothesis followed by post-hoc tests of specific effects. It is not well known that under certain circumstances this leads to a drastically inflated rate of type 1 error. It is even less well known that this procedure can also lead to an even lessor known type IV error (incorrect interpretation of a correctly rejected hypothesis)!\r\n\r\nIt is possible to avoid these dragons by using an alternative procedure where all inferences are derived from simultaneous confidence intervals (SCIs) on contrasts of interest. This approach provides interval inferences on effect sizes and it also ensures that the familywise type 1 error rate associated with directional inferences (the inferences usually derived from tests of null hypotheses) is controlled at alpha. One piece of software (PSY) can produce SCIs appropriate for planned analyses (where contrasts are defined independently of the data) and for more flexible analyses where contrasts are defined on a post hoc basis. However, this software is only available for use on windows and cannot be scripted into reproducible workflows.\r\n\r\nWe have been building an R package that implements the functions of PSY, and to make this method of statistical inference available to the masses! We are ready for you to play with some of the functions to analyse your own data, and create Quarto documents that document your workflow, to help future users. If you are feeling hacky enough, we could also use help developing further the R package, which is around 80% finished right now.\r\n\r\n\r\n\r\n"
}