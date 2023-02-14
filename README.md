# shellfmt
binary to shellcode formatter

# example
![image](https://user-images.githubusercontent.com/42578480/218708138-6d232a3b-665a-460d-a380-7c7a86714cd5.png)

# usage
```
[options]
-a: shellfmt -a "0d0f0900f0"   // load from argument
-c: shellfmt -c                // load from console
-f: shellfmt -f dir/filename   // load from file
```
# setup
```
git clone git@github.com:trimscash/shellfmt.git ~
echo "export PATH=$PATH:$HOME/shellfmt" >> ~/.zshrc
```
Replace `.zshrc` with the one you are using


