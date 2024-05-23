# Relevant Links

## Starfield Resources
- [Inara.cz Star Systems](https://inara.cz/starfield/starsystems-list/): Collect system names and associated URLs.
- [Starfield Wiki](https://starfieldwiki.net/wiki/Starfield:Star_Systems): Systems, planets, moons. - [Starfield Wiki](https://starfieldwiki.net/wiki/Starfield:Al-Battani_System) System, planet, type, gravity, temperature, atmosphere, magnetosphere, fauna (true/false - amount), (true/false - amount), water, resources, traits, Biomes.
- [Starfield wiki star systems](https://starfieldwiki.net/wiki/Starfield:Star_Systems) (try this one at some point)

## Scrapy Documentation
- [Scrapy Official Documentation](https://docs.scrapy.org/en/latest/): Official Scrapy documentation for reference.

## Other Resources
- [XPath Cheat Sheet](https://devhints.io/xpath): Handy XPath syntax cheat sheet.




## Possibly good urls
 - https://hardcoregamer.com/db/starfield-all-locations-systems-planets-moons/464902/#all-systems-in-starfield   All planets  look for <h2 id="all-planets-amp-moons-in-starfield">All Planets &amp; Moons in Starfield</h2> then this- //*[@id="article-body"]/div[1]/div[16] - collect coloumn 4 in system item , traverse each planet link coloumn 1, collect column 1 in planet item, column 2 in resource item, ignore column 3.  //*[@id="article-body"]/div[1]/div[16]