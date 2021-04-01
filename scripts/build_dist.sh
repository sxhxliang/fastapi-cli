###
 # @Descripttion: https://github.com/sxhxliang
 # @version: 0.0.1
 # @Author: Shihua Liang (sxhx.liang@gmail.com)
 # @FilePath: /fastapi-cli/scripts/build_dist.sh
 # @Create: 2021-04-01 15:05:05
 # @LastAuthor: Shihua Liang
 # @lastTime: 2021-04-01 16:07:50
### 

pandoc --from=markdown --to=rst --output=README.rst README.md
pip3 install --user --upgrade setuptools wheel twine
python3 setup.py sdist bdist_wheel
# python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
twine check dist/*
python3 -m twine upload dist/*
