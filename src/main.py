import os
import parents
import sitemap
import ru.parents

def main():
    directory = os.getcwd().replace("src", "")
    
    parents.update_en(f"{directory}\\en")
    ru.parents.update_ru(f"{directory}")
    sitemap.generate_sitemap()
    sitemap.generate_base_sitemap()

if __name__ == "__main__":
    main()
