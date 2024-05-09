FROM python:3.12
WORKDIR /calculator
RUN mkdir /calculator/app
RUN mkdir /calculator/source_code
COPY . /calculator/source_code
#RUN cd /calculator/source_code; python build.py --jenkins --clean --build_executable
#RUN mv /calculator/source_code/build /calculator/app/.
#RUN mv /calculator/source_code/dist /calculator/app/.
ENTRYPOINT ["echo", "Welcome to Vs Calculator\n @Vimantha Perera - All rights reserved ©"]