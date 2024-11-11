{
  "Title": "ME-mppca: Building a tensor-based thermal denoising method",
  "link_to_issue": "https://github.com/brainhackorg/global2024/issues/21",
  "issue_number": 21,
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
      "name": "hub:donostia_esp",
      "description": "",
      "color": "0E8A16"
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
      "name": "tools:Nipype",
      "description": "",
      "color": "EA1D4E"
    },
    {
      "name": "topic:MR_methodologies",
      "description": "",
      "color": "FBCA04"
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
  "content": "### Title\n\nME-mppca: Building a tensor-based thermal denoising method \n\n### Leaders\n\nMarco Antonio Flores-Coronado @MarcoFloresCoro \n\n### Collaborators\n\nSPiN lab (BCBL)\n\n### Brainhack Global 2024 Event\n\nBrainhack Donostia\n\n### Project Description\n\n- We are building a FOS library to do thermal noise reduction suited for Multi-echo acquisitions\r\n- This will be a Python implementation of (Tensor Denoising of Multidimensional MRI Data - Olesen - 2023 - Magnetic Resonance in Medicine - Wiley Online Library). Working with python possibilitates future integration with TEDANA\r\n-  https://github.com/SPiN-Lab/ME-PCA\r\n- Suggested reading are:\r\nTensor denoising of multidimensional MRI data\u2014Olesen\u20142023\u2014Magnetic Resonance in Medicine\u2014Wiley Online Library. (n.d.). Retrieved May 2, 2024, from https://onlinelibrary.wiley.com/doi/10.1002/mrm.29478\r\nHerthum, H., & Hetzer, S. (2024). Tensor denoising of quantitative multi-parameter mapping. Magnetic Resonance in Medicine, 92(1), 145\u2013157. https://doi.org/10.1002/mrm.30050\r\nVeraart, J., Novikov, D. S., Christiaens, D., Ades-aron, B., Sijbers, J., & Fieremans, E. (2016). Denoising of diffusion MRI using random matrix theory. NeuroImage, 142, 394\u2013406. https://doi.org/10.1016/j.neuroimage.2016.08.016\r\noriginal matlab implementation:\r\nhttps://github.com/Neurophysics-CFIN/MP-PCA-Denoising\r\nhttps://github.com/Neurophysics-CFIN/Tensor-MP-PCA\r\n\n\n### Link to project repository/sources\n\n.\n\n### Goals for Brainhack Global\n\n1-Create function that takes tensor and creates a sliding window for analysis\r\n2-Create function that performs  higher-order singular value decomposition (HOSVD)\r\n3-Documentation for library\n\n### Good first issues\n\n.\n\n### Communication channels\n\nhttps://mattermost.brainhack.org/brainhack/channels/me-pca\n\n### Skills\n\n-Python\r\n-Knowledge or will to learn Random Matrix Theory\r\n-Basic understanding of ME-fMRI\n\n### Onboarding documentation\n\n_No response_\n\n### What will participants learn?\n\nMatrix random theory alongside MPPCA denoising \n\n### Data to use\n\n_No response_\n\n### Number of collaborators\n\nmore\n\n### Credit to collaborators\n\nProject contributors are listed on the contributors list\n\n### Image\n\nLeave this text if you don't have an image yet.\n\n### Type\n\ncoding_methods, method_development\n\n### Development status\n\n0_concept_no_content\n\n### Topic\n\nMR_methodologies\n\n### Tools\n\nNipype\n\n### Programming language\n\nPython\n\n### Modalities\n\nfMRI\n\n### Git skills\n\n1_commit_push, 2_branches_PRs\n\n### Anything else?\n\n_No response_\n\n### Things to do after the project is submitted and ready to review.\n\n- [X] Add a comment below the main post of your issue saying: `Hi @brainhackorg/project-monitors my project is ready!`\n- [X] Twitter-sized summary of your project pitch.",
  "project_description": "\n\n- We are building a FOS library to do thermal noise reduction suited for Multi-echo acquisitions\r\n- This will be a Python implementation of (Tensor Denoising of Multidimensional MRI Data - Olesen - 2023 - Magnetic Resonance in Medicine - Wiley Online Library). Working with python possibilitates future integration with TEDANA\r\n-  https://github.com/SPiN-Lab/ME-PCA\r\n- Suggested reading are:\r\nTensor denoising of multidimensional MRI data\u2014Olesen\u20142023\u2014Magnetic Resonance in Medicine\u2014Wiley Online Library. (n.d.). Retrieved May 2, 2024, from https://onlinelibrary.wiley.com/doi/10.1002/mrm.29478\r\nHerthum, H., & Hetzer, S. (2024). Tensor denoising of quantitative multi-parameter mapping. Magnetic Resonance in Medicine, 92(1), 145\u2013157. https://doi.org/10.1002/mrm.30050\r\nVeraart, J., Novikov, D. S., Christiaens, D., Ades-aron, B., Sijbers, J., & Fieremans, E. (2016). Denoising of diffusion MRI using random matrix theory. NeuroImage, 142, 394\u2013406. https://doi.org/10.1016/j.neuroimage.2016.08.016\r\noriginal matlab implementation:\r\nhttps://github.com/Neurophysics-CFIN/MP-PCA-Denoising\r\nhttps://github.com/Neurophysics-CFIN/Tensor-MP-PCA\r\n\n\n"
}