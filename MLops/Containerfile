FROM quay.io/modh/odh-generic-data-science-notebook:v2

# Install Python packages and Jupyterlab extensions from Pipfile.lock
COPY Pipfile.lock ./

RUN echo "Installing softwares and packages" && micropipenv install && rm -f ./Pipfile.lock

# Fix permissions to support pip in Openshift environments
RUN chmod -R g+w /opt/app-root/lib/python3.9/site-packages && \
    fix-permissions /opt/app-root -P
