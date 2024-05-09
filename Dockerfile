FROM node:18-alpine
WORKDIR /calculator
RUN mkdir /calculator/app
RUN mkdir /calculator/source_code
COPY build /calculator/app/.
COPY dist /calculator/app/.
COPY args.py /calculator/source_code/.
COPY build.py /calculator/source_code/.
COPY calc.py /calculator/source_code/.
COPY test _calc.py /calculator/source_code/.
COPY Jenkinsfile /calculator/source_code/.
COPY requirements.txt /calculator/source_code/.
COPY README.md /calculator/source_code/.
COPY Dockerfile /calculator/source_code/.

CMD ["ls", "-la"]