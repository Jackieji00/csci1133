# CSCI 1133 Homework1
# Peiqi Ji
# Problem 1A
def focalLength (od,imd):
    answer = od ** -1 + imd ** -1
    answer = answer ** -1
    print("the focal length:" + str(answer) + " mm")
def main():
    print("Welcome to the Focal Length Calculator!")
    od = float(input("enter an object distance(mm): "))
    imd = float(input("enter an image  distance(mm): "))
    focalLength(od,imd)
if __name__ == '__main__':
    main()
