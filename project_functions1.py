{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "bf9fa557-1be2-4375-834f-9efe11435306",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "22e79a3c-f690-4485-b3b4-28231ace4ae3",
   "metadata": {},
   "outputs": [],
   "source": [
    "def load_and_process():\n",
    "\n",
    "\n",
    "        df1 = (\n",
    "                pd.read_csv(\"/Users/JeremyScarcella/project-group31-project/player_info.csv\")\n",
    "                .drop('height', axis=1)\n",
    "                .drop('birthCity', axis=1)\n",
    "                .drop('birthDate', axis=1)\n",
    "                .drop('birthStateProvince', axis=1)\n",
    "        )\n",
    "        \n",
    "        \n",
    "        \n",
    "        df2 = (\n",
    "                df1\n",
    "                .rename(columns={\"player_id\": \"Player ID\"})\n",
    "                .set_index('primaryPosition')                                       \n",
    "                .rename(index={\"D\": \"Defence\"})\n",
    "                .rename(index={\"G\": \"Goalie\"})\n",
    "                .rename(index={\"C\": \"Center\"})\n",
    "                .rename(index={\"RW\": \"Right Wing\"})\n",
    "                .rename(index={\"LW\": \"Left Wing\"})\n",
    "        )\n",
    "        \n",
    "        return df2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "feb5cb97-df10-404b-b9bf-f2ce48e10810",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Player ID</th>\n",
       "      <th>firstName</th>\n",
       "      <th>lastName</th>\n",
       "      <th>nationality</th>\n",
       "      <th>height_cm</th>\n",
       "      <th>weight</th>\n",
       "      <th>shootsCatches</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>primaryPosition</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Right Wing</th>\n",
       "      <td>8466148</td>\n",
       "      <td>Marian</td>\n",
       "      <td>Hossa</td>\n",
       "      <td>SVK</td>\n",
       "      <td>185.42</td>\n",
       "      <td>207.0</td>\n",
       "      <td>L</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Defence</th>\n",
       "      <td>8465058</td>\n",
       "      <td>Michal</td>\n",
       "      <td>Rozsival</td>\n",
       "      <td>CZE</td>\n",
       "      <td>185.42</td>\n",
       "      <td>210.0</td>\n",
       "      <td>R</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Defence</th>\n",
       "      <td>8476906</td>\n",
       "      <td>Shayne</td>\n",
       "      <td>Gostisbehere</td>\n",
       "      <td>USA</td>\n",
       "      <td>180.34</td>\n",
       "      <td>180.0</td>\n",
       "      <td>L</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Defence</th>\n",
       "      <td>8466285</td>\n",
       "      <td>Brian</td>\n",
       "      <td>Campbell</td>\n",
       "      <td>CAN</td>\n",
       "      <td>177.80</td>\n",
       "      <td>192.0</td>\n",
       "      <td>L</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Defence</th>\n",
       "      <td>8470607</td>\n",
       "      <td>Brent</td>\n",
       "      <td>Seabrook</td>\n",
       "      <td>CAN</td>\n",
       "      <td>190.50</td>\n",
       "      <td>220.0</td>\n",
       "      <td>R</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Left Wing</th>\n",
       "      <td>8479374</td>\n",
       "      <td>Adam</td>\n",
       "      <td>Mascherin</td>\n",
       "      <td>CAN</td>\n",
       "      <td>177.80</td>\n",
       "      <td>205.0</td>\n",
       "      <td>L</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Goalie</th>\n",
       "      <td>8479403</td>\n",
       "      <td>Tyler</td>\n",
       "      <td>Parsons</td>\n",
       "      <td>USA</td>\n",
       "      <td>185.42</td>\n",
       "      <td>185.0</td>\n",
       "      <td>L</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Defence</th>\n",
       "      <td>8480970</td>\n",
       "      <td>Marcus</td>\n",
       "      <td>Hogstrom</td>\n",
       "      <td>SWE</td>\n",
       "      <td>193.04</td>\n",
       "      <td>200.0</td>\n",
       "      <td>L</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Goalie</th>\n",
       "      <td>8477574</td>\n",
       "      <td>Parker</td>\n",
       "      <td>Milner</td>\n",
       "      <td>USA</td>\n",
       "      <td>185.42</td>\n",
       "      <td>185.0</td>\n",
       "      <td>L</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Center</th>\n",
       "      <td>8477352</td>\n",
       "      <td>Ryan</td>\n",
       "      <td>Fitzgerald</td>\n",
       "      <td>USA</td>\n",
       "      <td>175.26</td>\n",
       "      <td>172.0</td>\n",
       "      <td>R</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>3925 rows × 7 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                 Player ID firstName      lastName nationality  height_cm  \\\n",
       "primaryPosition                                                             \n",
       "Right Wing         8466148    Marian         Hossa         SVK     185.42   \n",
       "Defence            8465058    Michal      Rozsival         CZE     185.42   \n",
       "Defence            8476906    Shayne  Gostisbehere         USA     180.34   \n",
       "Defence            8466285     Brian      Campbell         CAN     177.80   \n",
       "Defence            8470607     Brent      Seabrook         CAN     190.50   \n",
       "...                    ...       ...           ...         ...        ...   \n",
       "Left Wing          8479374      Adam     Mascherin         CAN     177.80   \n",
       "Goalie             8479403     Tyler       Parsons         USA     185.42   \n",
       "Defence            8480970    Marcus      Hogstrom         SWE     193.04   \n",
       "Goalie             8477574    Parker        Milner         USA     185.42   \n",
       "Center             8477352      Ryan    Fitzgerald         USA     175.26   \n",
       "\n",
       "                 weight shootsCatches  \n",
       "primaryPosition                        \n",
       "Right Wing        207.0             L  \n",
       "Defence           210.0             R  \n",
       "Defence           180.0             L  \n",
       "Defence           192.0             L  \n",
       "Defence           220.0             R  \n",
       "...                 ...           ...  \n",
       "Left Wing         205.0             L  \n",
       "Goalie            185.0             L  \n",
       "Defence           200.0             L  \n",
       "Goalie            185.0             L  \n",
       "Center            172.0             R  \n",
       "\n",
       "[3925 rows x 7 columns]"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "load_and_process()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4bbf22a5-0beb-4e0f-87ea-74ca99ebf14c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
