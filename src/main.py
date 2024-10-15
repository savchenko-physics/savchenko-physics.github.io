import os
import parents
import ru.parents
import sitemap


def main():
    directory = os.getcwd().replace("src", "")
    
    parents.update_en(directory)
    ru.parents.update_ru(directory)
    sitemap.generate_sitemap()
    sitemap.generate_base_sitemap()

    print("Project updated!")

if __name__ == "__main__":
    main()