########
# Copyright (c) 2013 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    * See the License for the specific language governing permissions and
#    * limitations under the License.

from setuptools import setup

setup(
    name='cloudify-integration-tests',
    version='5.0.5',
    author='Cloudify',
    author_email='cosmo-admin@cloudify.co',
    packages=[
        'integration_tests',
        'integration_tests_plugins',
    ],
    description='Cloudify Integration Tests',
    zip_safe=False,
    install_requires=[
        'pika==0.11.2',
        'fasteners==0.13.0',
        'sh==1.11',
        'awscli==1.11.14',
        'docl',
        'docker==4.0.2',
        'GitPython==2.1.14',
        'PyGithub==1.45'
    ]
)
