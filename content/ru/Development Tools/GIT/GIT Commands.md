---
title: GIT Commands
---
[[ru/Development Tools/GIT/GIT Commands|RU]] | [[en/Development Tools/GIT/GIT Commands|EN]] | [[de/Development Tools/GIT/GIT Commands|DE]]

| **Command**                                                                                                                                                                 | **Description**                                                           |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| git init                                                                                                                                                                    | инициализация                                                             |
| git add *<br>git add text.txt<br>git rm text.txt<br>git mv oldname.txt newname.txt                                                                                          | добавить файлы<br>добавить файл<br>удалить файл  <br>переименование файла |
| git commit -m "first commit"                                                                                                                                                | коммит с комментарием                                                     |
| git remote add origin [https://github.com/path/name.git](https://github.com/path/name.git)<br><br>git remote set-url origin git@github.com-vibond:VIBondarenko/clavionx.git | добавить удаленный репозитарий<br><br>изменить удаленный репозитарий      |
| git push -u origin master                                                                                                                                                   | залить изменения в удаленный репозитарий                                  |
|                                                                                                                                                                             |                                                                           |
| git status                                                                                                                                                                  | Текущее состояние репозитория (изменения, неразрешенные конфликты и тп)   |
| git log --oneline                                                                                                                                                           | посмотреть все коммиты                                                    |
| git checkout .                                                                                                                                                              | восстановить все.                                                         |
| git checkout "код коммита"                                                                                                                                                  | вернуть до состояния этого коммита.                                       |
| git checkout master                                                                                                                                                         | вернуться в ветку мастер                                                  |
|                                                                                                                                                                             |                                                                           |
| git fetch --all<br><br>git reset --hard origin/master или<br><br>git reset --hard origin/<название_ветки>                                                                   | Восстановить файлы на локальном компьютере                                |
|                                                                                                                                                                             |                                                                           |
| git push origin                                                                                                                                                             | Замерджить все ветки локального репозитория на удаленный репозиторий      |
| git push origin master                                                                                                                                                      | Аналогично предыдущему, но делается пуш только ветки master               |
| git push origin HEAD                                                                                                                                                        | Запушить текущую ветку, не вводя целиком ее название                      |
| git pull origin                                                                                                                                                             | Замерджить все ветки с удаленного репозитория                             |


