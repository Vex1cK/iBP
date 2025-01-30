## Подкидываем нужный ip

в `.env` и `config` (ssh) в переменной FRONTEND_URL меняем ip на наш сервер

## Создание нового юзера

- `ssh root@ip` - вводим пароль, подключаемся к серверу
- `sudo adduser vex` (vex - имя юзера, можно любое другое) и придумываем пароль
- `sudo usermod -aG sudo vex`
- `sudo visudo`
- добавить строчку: `vex ALL=(ALL) NOPASSWD:ALL`, сохранить и выйти

## ssh ключи

### добавляем ключ на локальный комп

- В терминале (\cmd) заходим в `.ssh`
- создаём ключи на своём пк (если еще нет): `ssh-keygen -t rsa -b 4096 -f id_rsa_brieftalkai` и по желанию ставим passphrase
- копируем публичный ключ:
    - Windows: `type id_rsa_brieftalkai.pub` - копируем всё что выводится
    - Linux: `cat id_rsa_brieftalkai.pub` - копируем всё что выводится
- подключаемся к серверу
- `mkdir -p /home/vex/.ssh`
- `nano /home/vex/.ssh/authorized_keys`
- вставляем туда скопированный ключ, сохраняем и выходим
- `chmod 700 /home/vex/.ssh`
- `chmod 600 /home/vex/.ssh/authorized_keys`
- `sudo systemctl restart ssh`

```

```

На локальном пк:
- В папке `.ssh` создаём файл `config`
- Пишем туда:
```
Host server1
    HostName 45.8.249.209
    User vex
    IdentityFile C:\Users\Vex\.ssh\id_rsa_brieftalkai
```
- После этого можем подключаться к серверу так: `ssh server1`

### добавляем на сервер ssh ключ для гитхаб аккаунта (у меня приватная репа)

- На сервере пишем: `ssh-keygen -t rsa -b 4096 -C "github Vex1cK" -f ~/.ssh/id_rsa_github`
- `cat ~/.ssh/id_rsa_github.pub` - копируем, добавляем в настройках гитхаба
- проверяем доступ: `ssh -T git@github.com -i ~/.ssh/id_rsa_github`

### Настраиваем сервер

- `sudo nano /etc/ssh/sshd_config`
- меняем `PasswordAuthentication` на `no`
- меняем `PermitRootLogin` на `no`
- сохраняем выходим
- `sudo systemctl restart ssh`

### Рестартим сервер

- `sudo reboot`

## Запускаем шнягу

- `sudo apt update && sudo apt upgrade -y`
- `sudo apt-get install git`
- ставим docker:
    - `sudo apt-get install ca-certificates curl`
    - `sudo install -m 0755 -d /etc/apt/keyrings`
    - `sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc`
    - `sudo chmod a+r /etc/apt/keyrings/docker.asc`
    - вводим целиком:
    ```
    echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  ```
    - `sudo apt-get update`
    - `sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin`
    - Тестим: `sudo docker run hello-world`
- Клонируем и настраиваем репу:
    - `GIT_SSH_COMMAND="ssh -i ~/.ssh/id_rsa_github" git clone git@github.com:Vex1cK/Individual-Graduation-Project.git`
    - `cd Individual-Graduation-Project`
    - `git checkout dev`
    - `cd backend`
    - `mkdir -p ai_models/audio2text/whisper-large-v3`
    - `mkdir -p ai_models/text2text_summary/bert-large-uncased`

- Ставим драйвера для видюхи (если нужно):
    - `sudo apt install -y ubuntu-drivers-common alsa-utils`
    - `sudo ubuntu-drivers devices` - смотрим рекомендуемую версию драйвера
    - Если видюхшка на архитектуре Pascal: `sudo add-apt-repository ppa:graphics-drivers/ppa -y`
    - ```
        sudo apt update
        for kernel in $(linux-version list); do apt install -y "linux-headers-${kernel}"; done
      ```
    - `sudo apt install -y nvidia-driver-<driver_version>` например `sudo apt install -y nvidia-driver-550`
    - `nvidia-smi`
    - запрещаем обновления: `nano /etc/apt/apt.conf.d/50unattended-upgrades`
    - пишем: 
    ```
    Unattended-Upgrade::Package-Blacklist {
            "linux-";
            "nvidia-";
    };
   ```
    - Там еще куча нюансов с видюхой, я так и не смог поднять докер с доступом к видюхи потому что nvidia блокнули россию))))

- в `entrypoint.sh` нужно чекнуть стоит ли там скип контрольных сумм файлов
- `sudo docker compose up --build`

useful команда:

`GIT_SSH_COMMAND="ssh -i ~/.ssh/id_rsa_github" git pull`


## Че по времени
От создания сервера до запуска команды `sudo docker compose up --build` у меня ушло 18 минут

за минут 15 образы соберутся и поднимутся

## Ресурсы

- 4гб RAM - мало
- 8гб RAM - мало.
- 80ГБ ssd - МАЛО
- 4 CPU ядра - хватает

12гб не тестил