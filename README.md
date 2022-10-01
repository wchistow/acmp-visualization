# ACMP Visualization

## Использование

Все визуализации можно найти в каталоге results/.

## Запуск примеров на вашем копьютере:

### Установка:

#### Windows

```
cd
git clone https://gitflic.ru/project/wchistow/acmp-visualization.git
pip install -r acmp-visualization\requirements.txt
```

#### Linux, macOS

```
cd
git clone https://gitflic.ru/project/wchistow/acmp-visualization.git
pip install -r acmp-visualization/requirements.txt
```

### Подготовка

> Внимание! Этому коду потребуется **2,2 Гб** жесткого диска для загрузки данных.

```
cd acmp-visualization
python sort.py  # Займет некоторое количество времени.
```

### Запуск

#### Windows

```
python -m notebook
```

#### Linux, macOS

```
jupyter notebook
```

Теперь можно работать с примерами в Jupyter Notebook.
