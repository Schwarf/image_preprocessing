# image_preprocessing
## Description
The goal of this project to implement an extensible solution for preprocessing 
images of various file formats and create a tensorflow record for each image.    
## Coding rules
The code on master shall follow the following rules.
#### Software design
1. Each concrete implementation/class shall derive from one or more 
interfaces that define all public methods and properties.
2. For interface definition the library 'pure_interface' shall be used.
3. The software architecture/design shall follow the guidelines of CLEAN ARCHITECTURE (Robert C. Martin).
4. The software design shall follow the guidelines of CLEAN CODE (Robert C. Martin). 
#### Testing
1. Each concrete implementation/class shall have a corresponding test class.
2. All public methods or properties (including constructors) shall be tested by at least one (unit) test.
3. Tests shall be written using the 'pytest' framework. 
4. Tests on instances of composed objects shall be performed using the 'mock' framework. 
#### Code organization
1. Each module shall contain the folders "interfaces" and/or "implementations" and "tests".
2. The name of an interface file/class shall start with the prefix "i_"/"I".
3. The name of a test file/class shall start with the prefix "test_"/"Test".
