import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "jsii-calc",
    "version": "3.20.120",
    "description": "A simple calcuator built on JSII.",
    "license": "Apache-2.0",
    "url": "https://github.com/aws/jsii",
    "long_description_content_type": "text/markdown",
    "author": "Amazon Web Services",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/aws/jsii.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "jsii_calc",
        "jsii_calc._jsii",
        "jsii_calc.cdk16625",
        "jsii_calc.cdk16625.donotimport",
        "jsii_calc.composition",
        "jsii_calc.derived_class_has_no_properties",
        "jsii_calc.interface_in_namespace_includes_classes",
        "jsii_calc.interface_in_namespace_only_interface",
        "jsii_calc.jsii3656",
        "jsii_calc.module2530",
        "jsii_calc.module2617",
        "jsii_calc.module2647",
        "jsii_calc.module2689",
        "jsii_calc.module2689.methods",
        "jsii_calc.module2689.props",
        "jsii_calc.module2689.retval",
        "jsii_calc.module2689.structs",
        "jsii_calc.module2692",
        "jsii_calc.module2692.submodule1",
        "jsii_calc.module2692.submodule2",
        "jsii_calc.module2700",
        "jsii_calc.module2702",
        "jsii_calc.nodirect",
        "jsii_calc.nodirect.sub1",
        "jsii_calc.nodirect.sub2",
        "jsii_calc.onlystatic",
        "jsii_calc.python_self",
        "jsii_calc.submodule",
        "jsii_calc.submodule.back_references",
        "jsii_calc.submodule.child",
        "jsii_calc.submodule.isolated",
        "jsii_calc.submodule.nested_submodule",
        "jsii_calc.submodule.nested_submodule.deeply_nested",
        "jsii_calc.submodule.param",
        "jsii_calc.submodule.returnsparam"
    ],
    "package_data": {
        "jsii_calc._jsii": [
            "jsii-calc@3.20.120.jsii.tgz"
        ],
        "jsii_calc": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.7",
    "install_requires": [
        "jsii<0.0.1",
        "publication>=0.0.3",
        "scope.jsii-calc-base<0.0.1",
        "scope.jsii-calc-lib<0.0.1",
        "typeguard~=2.13.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Typing :: Typed",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved",
        "Test :: Classifier :: Is Dummy"
    ],
    "scripts": [
        "src/jsii_calc/_jsii/bin/calc"
    ]
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
