# Software-Engineering-Assignments
An interactive calculator to evaluate entered expression
*Contributors*
[Shi Su](https://github.com/JackySu)
[Shane Gilligan](https://github.com/gillyhigs)
[Alex Todeush](https://github.com/alex-todeush)
----------------------------------------------------------
# Usage
in terminal ```cd``` to the folder where you cloned the repository
## Webapp version
```bash
docker image build -t calculator_webapp -f Dockerfile.Webapp .
docker run -p 5000:5000 -d calculator_webapp
```
open localhost:5000 and enjoy :)

## CLI version
```bash
docker image build -t calculator_cli -f Dockerfile.CLI .
docker run -it calculator_cli
```
you can now interact with the calculator app in terminal
