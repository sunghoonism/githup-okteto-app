# Okteto Application example with automated github action
> 한글 Readme 파일을 보시려면 [여기](README_ko.md)를 눌러주세요.  

Applied site - https://api-sunghoonism.cloud.okteto.net/

## TL;DR:
Folk this repository and follow instructions
1. Get `okteto` Personal Access Token using "New Token" button of settings at https://cloud.okteto.com.
2. Make your repository secret with name `OKTETO_TOKEN` and value of `okteto` Personal Acess Token.  
   (You can make the repository secret with "New repository secret" button at Settings -> Secrets menu of your 'folked' repository)
3. Modify 19, 24 lines in .github/workflows/workflow.yml to your own `okteto` namespace.  
<h3> That's it! </h3>
