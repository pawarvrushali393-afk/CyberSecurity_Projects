{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "0edd20bf-f1dd-4028-a8b7-e250e29cadad",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Model Accuracy: 66.67 %\n",
      "\n",
      "Confusion Matrix:\n",
      "[[1 0]\n",
      " [1 1]]\n"
     ]
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAhcAAAHFCAYAAABBx9vxAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjkuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8hTgPZAAAACXBIWXMAAA9hAAAPYQGoP6dpAABAM0lEQVR4nO3deVyU5f7/8feAbCpggiBaKmoq5g5HRbPcy6XkZGVqqblbaYqWkeXWgpmpWblvaaWVnqw81JEWl45iqdgptSw3XEDEUgwVgbl/f/Rzvk2gstzDAPN6nsf9eMg191zXZ+ZEfvpcy20xDMMQAACASdycHQAAAChbSC4AAICpSC4AAICpSC4AAICpSC4AAICpSC4AAICpSC4AAICpSC4AAICpSC4AAICpSC5gqpUrV8pisdiucuXK6eabb9ajjz6qkydP5rpv165dN+yzffv2at++faHicFT/Zmnfvr3d9/XXq1atWk6L6e/fh8Vi0dSpU2/43r/G7+7urptuuklNmzbViBEjlJCQUKS4Xn75ZW3YsKFIfRRlnM2bN8tisWjz5s0OjwEo7co5OwCUTStWrFCDBg106dIlbd26VbGxsdqyZYt++OEHVahQoUB9zZ8/30FRFk//N1K7dm29++67udq9vLycEE3Rv4/7779f48ePl2EYSk9P148//qhVq1Zp8eLFGjNmjF5//fVC9fvyyy/r/vvvV1RUVJHiK+w4LVq00I4dO9SwYUOHjg+UBSQXcIhGjRopIiJCktShQwfl5OTohRde0IYNG9S/f/8C9eXof5k7+y8LHx8ftW7d2qkx/FVRv4/g4GC7z3PXXXdp7NixGj58uObNm6cGDRpo1KhRRQ2z2Pn5+ZWo/5+AkoxpERSLq/9SPnbsmF37hQsXNGrUKAUGBiogIED33XefTp06ZXdPXmX6BQsWqGnTpqpYsaJ8fX3VoEEDPfvss7nGLUz/R48elcVi0axZszR79myFhoaqYsWKioyMzLO0v2TJEtWrV09eXl5q2LCh3nvvPQ0aNMjUaY2r0zxfffWVhg0bpoCAAPn5+WnAgAHKyMhQSkqKHnzwQVWqVEkhISGaMGGCsrKy7PqYNm2aWrVqpcqVK8vPz08tWrTQsmXL9PdnFzpimsjd3V1vvvmmAgMD9eqrr9q9lp6ergkTJig0NFSenp6qXr26xo4dq4yMDNs9FotFGRkZevvtt23TLn+NMSUlRSNGjNDNN98sT09PhYaGatq0acrOzrYbKzMzU9OnT1dYWJi8vb0VEBCgDh06aPv27Tcc51rTIp988okiIyNVvnx5+fr6qkuXLtqxY4fdPVOnTpXFYtG+ffvUt29f+fv7Kzg4WIMHD9b58+eL+O0CJQ+VCxSLX3/9VZJUpUoVu/ahQ4eqR48eeu+993T8+HE99dRTevjhh/XVV19ds6+1a9fqscce0+jRozVr1iy5ubnp119/1f79+3PdW5j+r3rrrbfUoEEDzZ07V5L0/PPPq3v37jpy5Ij8/f0lSYsXL9aIESPUu3dvzZkzR+fPn9e0adOUmZmZ369GknL9JShJbm5ucnOzz/+HDh2q++67T2vXrlViYqKeffZZZWdn6+eff9Z9992n4cOH64svvtArr7yiatWqKTo62vbeo0ePasSIEapRo4YkKSEhQaNHj9bJkyc1efLkAsVbGD4+PurcubPWrl2rEydO6Oabb9bFixd155136sSJE3r22WfVpEkT7du3T5MnT9YPP/ygL774QhaLRTt27FDHjh3VoUMHPf/885L+rCRIfyYWLVu2lJubmyZPnqw6depox44devHFF3X06FGtWLFC0p/fcbdu3bRt2zaNHTtWHTt2VHZ2thISEpSUlKQ2bdpcd5y8vPfee+rfv7+6du2qNWvWKDMzUzNnzlT79u315Zdf6vbbb7e7v3fv3urTp4+GDBmiH374QTExMZKk5cuXm/59A05lACZasWKFIclISEgwsrKyjAsXLhgbN240qlSpYvj6+hopKSl29z322GN27585c6YhyUhOTra13Xnnncadd95p+/mJJ54wKlWqlK84CtP/kSNHDElG48aNjezsbFv7t99+a0gy1qxZYxiGYeTk5BhVq1Y1WrVqZTfGsWPHDA8PD6NmzZrXjfHq2JLyvIYMGZLr84wePdru/VFRUYYkY/bs2XbtzZo1M1q0aHHNcXNycoysrCxj+vTpRkBAgGG1Wq/5fRiGYUgypkyZcsPPI8l4/PHHr/n6xIkTDUnGzp07DcMwjNjYWMPNzc347rvv7O5bt26dIcmIi4uztVWoUMEYOHBgrj5HjBhhVKxY0Th27Jhd+6xZswxJxr59+wzDMIxVq1YZkowlS5Zc9zNca5yvv/7akGR8/fXXhmH8+R1Wq1bNaNy4sZGTk2O778KFC0ZQUJDRpk0bW9uUKVMMScbMmTPt+nzssccMb29vu+8fKAuYFoFDtG7dWh4eHvL19VXPnj1VtWpVffbZZwoODra7795777X7uUmTJpJyT5/8VcuWLXXu3Dn17dtXH3/8sdLS0q55b2H6v6pHjx5yd3e/5nt//vln23TEX9WoUUNt27a9Yf9X1alTR999912u6+p/Of9Vz5497X4OCwuzxfr39r9/xq+++kqdO3eWv7+/3N3d5eHhocmTJ+vs2bNKTU3Nd7xFYfxtCmbjxo1q1KiRmjVrpuzsbNt111135XtnxsaNG9WhQwdVq1bNro9u3bpJkrZs2SJJ+uyzz+Tt7a3Bgweb8ll+/vlnnTp1So888ohdhalixYrq3bu3EhISdPHiRbv35PXP4+XLl4vt+weKC9MicIhVq1YpLCxM5cqVU3BwsEJCQvK8LyAgwO7nqzskLl26dM2+H3nkEWVnZ2vJkiXq3bu3rFar/vGPf+jFF19Uly5ditx/ft979uxZScqVMF1tO3LkyA3HkCRvb2/b4tcbqVy5st3Pnp6e12y/fPmy7edvv/1WXbt2Vfv27bVkyRLb2oQNGzbopZdeytf3YYarCU+1atUkSadPn9avv/4qDw+PPO+/XuJ41enTp/Xpp5/esI8zZ86oWrVquaaaCuvq//95/bNdrVo1Wa1W/f777ypfvrytvSj/PAKlCckFHCIsLCzff2EWxqOPPqpHH31UGRkZ2rp1q6ZMmaKePXvq4MGDqlmzpsPG/aurf1GcPn0612spKSnFEkN+rV27Vh4eHtq4caO8vb1t7cVxbsRVly5d0hdffKE6dero5ptvliQFBgbKx8fnmmsOAgMDb9hvYGCgmjRpopdeeinP168mMlWqVNE333wjq9VqSoJx9f//5OTkXK+dOnVKbm5uuummm4o8DlAaMS2CUq1ChQrq1q2bJk2apCtXrmjfvn3FNnb9+vVVtWpVffDBB3btSUlJtt0HJcXVA83+Os1z6dIlrV69uljGz8nJ0RNPPKGzZ89q4sSJtvaePXvq0KFDCggIUERERK7rrztuvLy88vwv/J49e+rHH39UnTp18uzjanLRrVs3Xb58WStXrrxurNca5+/q16+v6tWr67333rOb7snIyND69ettO0gAV0TlAqXOsGHD5OPjo7Zt2yokJEQpKSmKjY2Vv7+//vGPfxRbHG5ubpo2bZpGjBih+++/X4MHD9a5c+c0bdo0hYSE5Pu/ji9dunTN0yvNOlehR48emj17tvr166fhw4fr7NmzmjVrlkMO6jp9+rQSEhJkGIYuXLhgO0Tr+++/17hx4zRs2DDbvWPHjtX69et1xx13aNy4cWrSpImsVquSkpK0adMmjR8/Xq1atZIkNW7cWJs3b9ann36qkJAQ+fr6qn79+po+fbri4+PVpk0bjRkzRvXr19fly5d19OhRxcXFaeHChbr55pvVt29frVixQiNHjtTPP/+sDh06yGq1aufOnQoLC9NDDz103XH+zs3NTTNnzlT//v3Vs2dPjRgxQpmZmXr11Vd17tw5zZgxw/TvFigtSC5Q6rRr104rV67UBx98oN9//12BgYG6/fbbtWrVqlxbXR1t+PDhslgsmjlzpv75z3+qVq1aeuaZZ/Txxx8rKSkpX30cPnxYkZGReb6WlZWlcuWK/mvasWNHLV++XK+88oruueceVa9eXcOGDVNQUJCGDBlS5P7/at26dVq3bp3c3NxUsWJF1axZU5GRkVq4cGGuZKlChQratm2bZsyYocWLF+vIkSPy8fFRjRo11LlzZ7vKxeuvv67HH39cDz30kG0L6+bNmxUSEqJdu3bphRde0KuvvqoTJ07I19dXoaGhuvvuu21TE+XKlVNcXJxiY2O1Zs0azZ07V76+vmratKnuvvvuG46Tl379+qlChQqKjY1Vnz595O7urtatW+vrr79WmzZtTP1egdLEYvx9+TaAIjl37pzq1aunqKgoLV682NnhAECxo3IBFEFKSopeeukldejQQQEBATp27JjmzJmjCxcu6Mknn3R2eADgFCQXQBF4eXnp6NGjeuyxx/Tbb7+pfPnyat26tRYuXKjbbrvN2eEBgFMwLQIAAEzFVlQAAMqorVu36p577lG1atVksVjydbbNli1bFB4eLm9vb9WuXVsLFy4s8LgkFwAAlFEZGRlq2rSp3nzzzXzdf+TIEXXv3l3t2rWzPRxxzJgxWr9+fYHGZVoEAAAXYLFY9NFHHykqKuqa90ycOFGffPKJDhw4YGsbOXKkvv/+e+3YsSPfY1G5AACglMjMzFR6errdlZmZaVr/O3bsUNeuXe3a7rrrLu3atUtZWVn57qdM7hbJSjvs7BCAEsmnWjtnhwCUONlXTjp8DLP+Xop9c5WmTZtm1zZlyhRNnTrVlP5TUlJyPYwxODhY2dnZSktLu+ZDKP+uTCYXAACURTExMYqOjrZrM/sYf4vFYvfz1dUTf2+/HpILAAAczZpjSjdeXl4OeSbQVVWrVs31VOfU1FSVK1fO9iTg/CC5AADA0QyrsyPIl8jISH366ad2bZs2bVJERIQ8PDzy3Q8LOgEAcDSr1ZyrgP744w/t3btXe/fulfTnVtO9e/faHqwYExOjAQMG2O4fOXKkjh07pujoaB04cEDLly/XsmXLNGHChAKNS+UCAIAyateuXerQoYPt56vrNQYOHKiVK1cqOTnZ7gnOoaGhiouL07hx4/TWW2+pWrVqmjdvnnr37l2gccvkORfsFgHyxm4RILfi2C1y5dQ+U/rxrFY6nllE5QIAAEcrxJRGacaaCwAAYCoqFwAAOFop2S1iFpILAAAczaRzLkoLpkUAAICpqFwAAOBoTIsAAABTsVsEAACg8KhcAADgYAbTIgAAwFQuNi1CcgEAgKO5WOWCNRcAAMBUVC4AAHA0FztEi+QCAABHY1oEAACg8KhcAADgaOwWAQAApmJaBAAAoPCoXAAA4GhMiwAAADMZhmttRWVaBAAAmIrKBQAAjuZiCzpJLgAAcDTWXAAAAFO5WOWCNRcAAMBUVC4AAHA0HlwGAABMxbQIAABA4VG5AADA0dgtAgAATMW0CAAAQOFRuQAAwNGYFgEAAKZyseSCaREAAGAqKhcAADiYqz1yneQCAABHc7FpEZILAAAcja2oAAAAhUflAgAAR2NaBAAAmIppEQAAgMKjcgEAgKMxLQIAAEzFtAgAAEDhUbkAAMDRmBYBAACmcrHkgmkRAABgKioXAAA4most6CS5AADA0VxsWoTkAgAAR3OxygVrLgAAgKmoXAAA4GhMiwAAAFMxLQIAAFB4VC4AAHA0pkUAAICpXCy5YFoEAACYisoFAACOZhjOjqBYkVwAAOBoTIsAAAAUXomoXERHR+fZbrFY5O3trbp166pXr16qXLlyMUcGAIAJXKxyUSKSi8TERO3Zs0c5OTmqX7++DMPQL7/8Ind3dzVo0EDz58/X+PHj9c0336hhw4bODhcAgILhEK3i16tXL3Xu3FmnTp3S7t27tWfPHp08eVJdunRR3759dfLkSd1xxx0aN26cs0MFAKDgrFZzrlKiRCQXr776ql544QX5+fnZ2vz8/DR16lTNnDlT5cuX1+TJk7V7924nRgkAQOkzf/58hYaGytvbW+Hh4dq2bdt173/33XfVtGlTlS9fXiEhIXr00Ud19uzZAo1ZIpKL8+fPKzU1NVf7mTNnlJ6eLkmqVKmSrly5UtyhAQBQdIZhzlVA77//vsaOHatJkyYpMTFR7dq1U7du3ZSUlJTn/d98840GDBigIUOGaN++ffrwww/13XffaejQoQUat0QkF7169dLgwYP10Ucf6cSJEzp58qQ++ugjDRkyRFFRUZKkb7/9VvXq1XNuoAAAFIaTpkVmz56tIUOGaOjQoQoLC9PcuXN1yy23aMGCBXnen5CQoFq1amnMmDEKDQ3V7bffrhEjRmjXrl0FGrdEJBeLFi1Sp06d9NBDD6lmzZqqUaOGHnroIXXq1EkLFy6UJDVo0EBLly51cqQAADhPZmam0tPT7a7MzMw8771y5Yp2796trl272rV37dpV27dvz/M9bdq00YkTJxQXFyfDMHT69GmtW7dOPXr0KFCcJSK5qFixopYsWaKzZ8/ado6cPXtWixcvVoUKFSRJzZo1U7NmzZwbKAAAhWFS5SI2Nlb+/v52V2xsbJ5DpqWlKScnR8HBwXbtwcHBSklJyfM9bdq00bvvvqs+ffrI09NTVatWVaVKlfTGG28U6OOWiOTiqooVK6pJkyZq2rSpKlas6OxwAAAwh2E15YqJidH58+ftrpiYmOsObbFY7EMxjFxtV+3fv19jxoyxbaL4/PPPdeTIEY0cObJAH7dEnHORkZGhGTNm6Msvv1Rqaqqsf5tXOnz4sJMiAwCg5PDy8pKXl1e+7g0MDJS7u3uuKkVqamquasZVsbGxatu2rZ566ilJUpMmTVShQgW1a9dOL774okJCQvI1dolILoYOHaotW7bokUceUUhIyDUzKgAASiPDWvwPLvP09FR4eLji4+P1z3/+09YeHx+vXr165fmeixcvqlw5+9TA3d1d0p8Vj/wqEcnFZ599pn//+99q27ats0MBAMB8TjoAKzo6Wo888ogiIiIUGRmpxYsXKykpyTbNERMTo5MnT2rVqlWSpHvuuUfDhg3TggULdNdddyk5OVljx45Vy5YtVa1atXyPWyKSi5tuuonnhgAAYLI+ffro7Nmzmj59upKTk9WoUSPFxcWpZs2akqTk5GS7My8GDRqkCxcu6M0339T48eNVqVIldezYUa+88kqBxrUYBalzOMg777yjjz/+WG+//bbKly9f5P6y0lijAeTFp1o7Z4cAlDjZV046fIyLC0ab0k/5UQXbteEsJaJy8dprr+nQoUMKDg5WrVq15OHhYff6nj17nBQZAAAmcMKaC2cqEcnF1VM4AQAok0rRQ8fMUCKSiylTpjg7BAAAYJISkVwAAFCmUbkoHpUrV9bBgwcVGBiom2666bpnW/z222/FGBkAACZz/t6JYuW05GLOnDny9fWVJM2dO9dZYQAAAJM5LbkYOHBgnn9G2bBr7w9a8d467f/pV505+5tej31ene5o4+ywAKcbOWKgxkePVEhIkPbtP6jx46fom/9+6+yw4GhMiziH1WrVr7/+muezRe644w4nRYXCunTpsurXra2o7l01btKLzg4HKBEeeOBezX5tqp4Y/ay27/hOw4Y+oo2fvqPGTdvr+PFTzg4PjsRW1OKXkJCgfv366dixY7nOLrdYLMrJyXFSZCisdpH/ULvIfzg7DKBEGffkMC1fsVbLV6yRJI2fMEVdu96pkSMGaNJzM5wcHWCeEvHI9ZEjRyoiIkI//vijfvvtN/3++++2i8WcAMoCDw8PtWjRRPFfbLFrj4/fosjWEU6KCsXGpEeulxYlonLxyy+/aN26dapbt66zQwEAhwgMrKxy5cop9XSaXXtqapqCqwY5KSoUG6ZFil+rVq3066+/Fiq5yMzMVGZmpl2bW2Zmvp93DwDFKa+p3xLwiCfAVE5LLv73v//Z/jx69GiNHz9eKSkpaty4ca5nizRp0uSa/cTGxmratGl2bc89NUaTn37S3IABoAjS0n5Tdna2gqtWsWuvUiVAqafPOCkqFBeD3SLFo1mzZrky9sGDB9v+fPW1Gy3ojImJUXR0tF2b2wXHP+EOAAoiKytLe/b8T5073aGPP/7c1t658x369NP/ODEyFAumRYrHkSNHTOnHy8sr1xRI1pW0a9yN4nLx4iUlnfi/rXUnT53WTwcPyd/PVyHML8NFzXl9id5e8bp27/5eCTt3a9iQh1XjlupatHi1s0ODo5WixZhmcFpyUbNmTWcNjWLw40+/aPDoibafZ76xWJLUq1tnvfTceGeFBTjVhx9+ooDKN+m5SeMUEhKkH/f9rHvufURJSVRbUbZYjBKwkujtt99WYGCgevToIUl6+umntXjxYjVs2FBr1qwpcCKSlXbYEWECpZ5PtXbODgEocbKvOD65y5je35R+Kkx+15R+HK1EnHPx8ssvy8fHR5K0Y8cOvfnmm5o5c6YCAwM1btw4J0cHAEARWa3mXKVEidiKevz4cds21A0bNuj+++/X8OHD1bZtW7Vv3965wQEAgAIpEZWLihUr6uzZs5KkTZs2qXPnzpIkb29vXbp0yZmhAQBQdFbDnKuUKBGViy5dumjo0KFq3ry5Dh48aFt7sW/fPtWqVcu5wQEAUFQutlukRFQu3nrrLUVGRurMmTNav369AgICJEm7d+9W3759nRwdAAAoiBKxW8Rs7BYB8sZuESC3YtktMukBU/qp8NKHpvTjaE49/rtRo0Zyc3OzOwo8L9c7/hsAgJKO47+LSbNmzZSSkqKgoKA8jwLP7/HfAACgZHHq8d9VqlSx/RkAgDKrFO30MEOJOP6bo8ABAGUayYVzHDx4UJs3b1Zqaqqsf5ubmjx5spOiAgDABC62FbVEJBdLlizRqFGjFBgYqKpVq8pisdhes1gsJBcAAJQiJSK5ePHFF/XSSy9p4sSJN74ZAIDShmmR4vf777/rgQfM2QMMAEBJY7hYclEiTuh84IEHtGnTJmeHAQAATOC0ysW8efNsf65bt66ef/55JSQkqHHjxvLw8LC7d8yYMcUdHgAA5nGxyoXTjv8ODQ3N130Wi0WHDxfsOG+O/wbyxvHfQG7Fcfz3hSe6m9KP75txpvTjaE49RCsvV3Odv+4YAQAApUeJWHMhScuWLVOjRo3k7e0tb29vNWrUSEuXLnV2WAAAFJ3VMOcqJUrEbpHnn39ec+bM0ejRoxUZGSlJ2rFjh8aNG6ejR4/qxRdfdHKEAAAUQSlKDMxQIh65HhgYqDfeeEN9+/a1a1+zZo1Gjx6ttLS0AvXHmgsgb6y5AHIrljUXI+82pR/fhZ+b0o+jlYjKRU5OjiIiInK1h4eHKzs72wkRAQBgnhLw3/HFqkSsuXj44Ye1YMGCXO2LFy9W//79nRARAAAmYs2FcyxbtkybNm1S69atJUkJCQk6fvy4BgwYoOjoaNt9s2fPdlaIAAAUTilKDMxQIpKLH3/8US1atJAkHTp0SJJUpUoVValSRT/++KPtPranAgBQ8pWI5OLrr792dggAADiMqz1bpEQkFwAAlGkullyUiAWdAACg7KByAQCAo1mdHUDxIrkAAMDBXG3NBdMiAADAVFQuAABwNBerXJBcAADgaC625oJpEQAAYCoqFwAAOJirLegkuQAAwNFcbFqE5AIAAAdztcoFay4AAICpqFwAAOBoTIsAAAAzGS6WXDAtAgAATEXlAgAAR3OxygXJBQAADsa0CAAAQBFQuQAAwNFcrHJBcgEAgIMxLQIAAExlWM25CmP+/PkKDQ2Vt7e3wsPDtW3btuven5mZqUmTJqlmzZry8vJSnTp1tHz58gKNSeUCAIAy6v3339fYsWM1f/58tW3bVosWLVK3bt20f/9+1ahRI8/3PPjggzp9+rSWLVumunXrKjU1VdnZ2QUa12IYRpk78Dwr7bCzQwBKJJ9q7ZwdAlDiZF856fAxTne405R+gr/eUqD7W7VqpRYtWmjBggW2trCwMEVFRSk2NjbX/Z9//rkeeughHT58WJUrVy50nEyLAADgaIbFlCszM1Pp6el2V2ZmZp5DXrlyRbt371bXrl3t2rt27art27fn+Z5PPvlEERERmjlzpqpXr6569eppwoQJunTpUoE+LskFAAClRGxsrPz9/e2uvCoQkpSWlqacnBwFBwfbtQcHByslJSXP9xw+fFjffPONfvzxR3300UeaO3eu1q1bp8cff7xAcbLmAgAABzNrt0hMTIyio6Pt2ry8vK77HovFYh+LYeRqu8pqtcpisejdd9+Vv7+/JGn27Nm6//779dZbb8nHxydfcZJcAADgYIY177/MC8rLy+uGycRVgYGBcnd3z1WlSE1NzVXNuCokJETVq1e3JRbSn2s0DMPQiRMndOutt+ZrbKZFAAAogzw9PRUeHq74+Hi79vj4eLVp0ybP97Rt21anTp3SH3/8YWs7ePCg3NzcdPPNN+d7bJILAAAczFnnXERHR2vp0qVavny5Dhw4oHHjxikpKUkjR46U9Oc0y4ABA2z39+vXTwEBAXr00Ue1f/9+bd26VU899ZQGDx6c7ykRiWkRAAAczjDMmRYpqD59+ujs2bOaPn26kpOT1ahRI8XFxalmzZqSpOTkZCUlJdnur1ixouLj4zV69GhFREQoICBADz74oF588cUCjcs5F4AL4ZwLILfiOOfiZGRHU/qpvuMrU/pxNCoXAAA4mKs9W4TkAgAABzNrt0hpQXIBAICDlb0FCNfHbhEAAGAqKhcAADgY0yIAAMBUrpZcMC0CAABMReUCAAAHc7UFnSQXAAA4GNMiAAAARUDlAgAAB3PWs0WcJV/JxSeffJLvDu+9995CBwMAQFnE8d95iIqKyldnFotFOTk5RYkHAACUcvlKLqxWF0u5AAAwkZVpEQAAYCbWXORDRkaGtmzZoqSkJF25csXutTFjxpgSGAAAZYWrbUUtcHKRmJio7t276+LFi8rIyFDlypWVlpam8uXLKygoiOQCAAAXV+BzLsaNG6d77rlHv/32m3x8fJSQkKBjx44pPDxcs2bNckSMAACUaoZhzlVaFDi52Lt3r8aPHy93d3e5u7srMzNTt9xyi2bOnKlnn33WETECAFCqGVaLKVdpUeDkwsPDQxbLnx8wODhYSUlJkiR/f3/bnwEAgOsq8JqL5s2ba9euXapXr546dOigyZMnKy0tTatXr1bjxo0dESMAAKWaq21FLXDl4uWXX1ZISIgk6YUXXlBAQIBGjRql1NRULV682PQAAQAo7QzDYspVWhS4chEREWH7c5UqVRQXF2dqQAAAoHTjEC0AABysNO30MEOBk4vQ0FDbgs68HD58uEgBAQBQ1rjamosCJxdjx461+zkrK0uJiYn6/PPP9dRTT5kVFwAAKKUKnFw8+eSTeba/9dZb2rVrV5EDAgCgrClNizHNUODdItfSrVs3rV+/3qzuAAAoM1zthE7TFnSuW7dOlStXNqs7AADKDNZc3EDz5s3tFnQahqGUlBSdOXNG8+fPNzU4AABQ+hQ4uejVq5ddcuHm5qYqVaqoffv2atCgganBATDXpVPbnB0C4JJcbc1FgZOLqVOnOiAMAADKLlebFinwgk53d3elpqbmaj979qzc3d1NCQoAAJReBa5cGNdYrpqZmSlPT88iBwQAQFlTijZ6mCLfycW8efMkSRaLRUuXLlXFihVtr+Xk5Gjr1q2suQAAIA+uNi2S7+Rizpw5kv6sXCxcuNBuCsTT01O1atXSwoULzY8QAACUKvlOLo4cOSJJ6tChg/71r3/ppptuclhQAACUJewWuYGvv/7aEXEAAFBmWZ0dQDEr8G6R+++/XzNmzMjV/uqrr+qBBx4wJSgAAFB6FTi52LJli3r06JGr/e6779bWrVtNCQoAgLLEkMWUq7Qo8LTIH3/8keeWUw8PD6Wnp5sSFAAAZYnVxfaiFrhy0ahRI73//vu52teuXauGDRuaEhQAAGWJVRZTrtKiwJWL559/Xr1799ahQ4fUsWNHSdKXX36p9957T+vWrTM9QAAAULoUOLm49957tWHDBr388stat26dfHx81LRpU3311Vfy8/NzRIwAAJRqpWm9hBksxrXO886nc+fO6d1339WyZcv0/fffKycnx6zYCi0r7bCzQwAAlBIegbUdPkZ8cB9T+ulyOveyhJKowGsurvrqq6/08MMPq1q1anrzzTfVvXt37dq1y8zYAABAKVSgaZETJ05o5cqVWr58uTIyMvTggw8qKytL69evZzEnAADX4GrTIvmuXHTv3l0NGzbU/v379cYbb+jUqVN64403HBkbAABlgtWkq7TId+Vi06ZNGjNmjEaNGqVbb73VkTEBAIBSLN+Vi23btunChQuKiIhQq1at9Oabb+rMmTOOjA0AgDLB1SoX+U4uIiMjtWTJEiUnJ2vEiBFau3atqlevLqvVqvj4eF24cMGRcQIAUGq52vHfBd4tUr58eQ0ePFjffPONfvjhB40fP14zZsxQUFCQ7r33XkfECAAASpFCb0WVpPr162vmzJk6ceKE1qxZY1ZMAACUKVaLOVdpUeATOvPi7u6uqKgoRUVFmdEdAABlSml6LogZTEkuAADAtbnYQ1GLNi0CAADwd1QuAABwsNK0jdQMJBcAADiY1eJaay6YFgEAAKaicgEAgIO52oJOkgsAABzM1dZcMC0CAABMReUCAAAHK02na5qBygUAAA5mlcWUqzDmz5+v0NBQeXt7Kzw8XNu2bcvX+/773/+qXLlyatasWYHHJLkAAKCMev/99zV27FhNmjRJiYmJateunbp166akpKTrvu/8+fMaMGCAOnXqVKhxSS4AAHAww6SroGbPnq0hQ4Zo6NChCgsL09y5c3XLLbdowYIF133fiBEj1K9fP0VGRhZiVJILAAAczqynomZmZio9Pd3uyszMzHPMK1euaPfu3eratatde9euXbV9+/ZrxrpixQodOnRIU6ZMKfTnJbkAAMDBrCZdsbGx8vf3t7tiY2PzHDMtLU05OTkKDg62aw8ODlZKSkqe7/nll1/0zDPP6N1331W5coXf88FuEQAASomYmBhFR0fbtXl5eV33PZa/HT1uGEauNknKyclRv379NG3aNNWrV69IcZJcAADgYGad0Onl5XXDZOKqwMBAubu756pSpKam5qpmSNKFCxe0a9cuJSYm6oknnpAkWa1WGYahcuXKadOmTerYsWO+xia5AADAwZxxzoWnp6fCw8MVHx+vf/7zn7b2+Ph49erVK9f9fn5++uGHH+za5s+fr6+++krr1q1TaGhovscmuQAAoIyKjo7WI488ooiICEVGRmrx4sVKSkrSyJEjJf05zXLy5EmtWrVKbm5uatSokd37g4KC5O3tnav9RkguAABwMGc9W6RPnz46e/aspk+fruTkZDVq1EhxcXGqWbOmJCk5OfmGZ14UhsUwjDL3sLastMPODgEAUEp4BNZ2+BiLbn7YlH5GnHjHlH4cja2oAADAVEyLAADgYIaLPbiM5AIAAAdz1poLZ2FaBAAAmIrKBQAADuZqlQuSCwAAHKzMbcu8AZILAAAczBkndDoTay4AAICpqFwAAOBgrLkAAACmcrXkgmkRAABgKioXAAA4GLtFAACAqdgtAgAAUARULgAAcDBXW9BJcgEAgIO52poLpkUAAICpqFwAAOBgVherXZBcAADgYKy5AAAApnKtugVrLgAAgMmoXAAA4GBMiwAAAFNxQicAAEARULkAAMDB2IoKAABM5VqpBdMiAADAZFQuAABwMHaLAAAAU7namgumRQAAgKmoXAAA4GCuVbcguQAAwOFYcwEAAEzFmgsAAIAioHIBAICDuVbdguQCAACHc7U1FyViWuTcuXNaunSpYmJi9Ntvv0mS9uzZo5MnTzo5MgAAUFBOr1z873//U+fOneXv76+jR49q2LBhqly5sj766CMdO3ZMq1atcnaIAAAUieFiEyNOr1xER0dr0KBB+uWXX+Tt7W1r79atm7Zu3erEyAAAMIfVpKu0cHpy8d1332nEiBG52qtXr66UlBQnRAQAAIrC6dMi3t7eSk9Pz9X+888/q0qVKk6ICAAAc3HORTHr1auXpk+frqysLEmSxWJRUlKSnnnmGfXu3dvJ0QEAUHSGSVdp4fTkYtasWTpz5oyCgoJ06dIl3Xnnnapbt658fX310ksvOTs8AABQQE6fFvHz89M333yjr776Snv27JHValWLFi3UuXNnZ4eGIti19weteG+d9v/0q86c/U2vxz6vTne0cXZYgFPxe+G6mBYpBpUrV1ZaWpokafDgwbpw4YI6duyoCRMm6OmnnyaxKAMuXbqs+nVr69nox5wdClBi8Hvhulxtt4hTKhdXrlxRenq6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OXOUnJysvXv3yt/f39nhAKYguUCBuLu7q2rVqqb15+PjIx8fH9P6A0qbQ4cOKTw8XLfeequzQwFMw7SIi2nfvr2eeOIJPfHEE6pUqZICAgL03HPP6a87ki9evKjBgwfL19dXNWrU0OLFi22v/X2q4/fff1f//v1VpUoV+fj46NZbb9WKFSvsxjx8+LA6dOig8uXLq2nTptqxY4fttb9Pi0ydOlXNmjXT6tWrVatWLfn7++uhhx7ShQsXbPdcuHBB/fv3V4UKFRQSEqI5c+aoffv2Gjt2rLlfFpBP69atU+PGjeXj46OAgAB17txZGRkZ+u6779SlSxcFBgbK399fd955p/bs2WN7X61atbR+/XqtWrVKFotFgwYNkiSdP39ew4cPV1BQkPz8/NSxY0d9//33Tvp0QMGRXLigt99+W+XKldPOnTs1b948zZkzR0uXLrW9/tprrykiIkKJiYl67LHHNGrUKP3000959vX8889r//79+uyzz3TgwAEtWLAg15TJpEmTNGHCBO3du1f16tVT3759lZ2dfc34Dh06pA0bNmjjxo3auHGjtmzZohkzZthej46O1n//+1998sknio+P17Zt2+z+hQ0Up+TkZPXt21eDBw/WgQMHtHnzZt13330yDEMXLlzQwIEDtW3bNiUkJOjWW29V9+7dbcnyd999p7vvvlsPPvigkpOT9frrr8swDPXo0UMpKSmKi4vT7t271aJFC3Xq1Em//fabkz8tkE8GXMqdd95phIWFGVar1dY2ceJEIywszDAMw6hZs6bx8MMP216zWq1GUFCQsWDBAsMwDOPIkSOGJCMxMdEwDMO45557jEcffTTPsa7eu3TpUlvbvn37DEnGgQMHDMMwjBUrVhj+/v6216dMmWKUL1/eSE9Pt7U99dRTRqtWrQzDMIz09HTDw8PD+PDDD22vnzt3zihfvrzx5JNPFuIbAYpm9+7dhiTj6NGjN7w3Ozvb8PX1NT799FNbW69evYyBAwfafv7yyy8NPz8/4/Lly3bvrVOnjrFo0SLT4gYcicqFC2rdurUsFovt58jISP3yyy/KycmRJDVp0sT2msViUdWqVZWamppnX6NGjdLatWvVrFkzPf3009q+fXuue/7aX0hIiCRdsz/pz1Kxr6+v3Xuu3n/48GFlZWWpZcuWttf9/f1Vv379635mwFGaNm2qTp06qXHjxnrggQe0ZMkS/f7775L+/Od85MiRqlevnvz9/eXv768//vjD7lkOf7d792798ccfCggIUMWKFW3XkSNHdOjQoeL6WECRsKATufz9sboWi0VWqzXPe7t166Zjx47p3//+t7744gt16tRJjz/+uGbNmpVnf1eTmmv1d6Pxjf+/NuSvydFf24Hi5u7urvj4eG3fvl2bNm3SG2+8oUmTJmnnzp16/PHHdebMGc2dO1c1a9aUl5eXIiMjdeXKlWv2Z7VaFRISos2bN+d6ja2qKC2oXLighISEXD/feuutcnd3L1R/VapU0aBBg/TOO+9o7ty5dgtAzVanTh15eHjo22+/tbWlp6frl19+cdiYwI1YLBa1bdtW06ZNU2Jiojw9PfXRRx9p27ZtGjNmjLp3767bbrtNXl5eSktLu25fLVq0UEpKisqVK6e6devaXWZtAQccjcqFCzp+/Liio6M1YsQI7dmzR2+88YZee+21QvU1efJkhYeH67bbblNmZqY2btyosLAwkyP+P76+vho4cKCeeuopVa5cWUFBQZoyZYrc3NxyVTOA4rBz5059+eWX6tq1q4KCgrRz506dOXNGYWFhqlu3rlavXq2IiAilp6frqaeeuuHW686dOysyMlJRUVF65ZVXVL9+fZ06dUpxcXGKiopSREREMX0yoPBILlzQgAEDdOnSJbVs2VLu7u4aPXq0hg8fXqi+PD09FRMTo6NHj8rHx0ft2rXT2rVrTY7Y3uzZszVy5Ej17NlTfn5+evrpp3X8+HF5e3s7dFwgL35+ftq6davmzp2r9PR01axZU6+99pq6deumqlWravjw4WrevLlq1Kihl19+WRMmTLhufxaLRXFxcZo0aZIGDx6sM2fOqGrVqrrjjjsUHBxcTJ8KKBoeue5i2rdvr2bNml33iO/SJiMjQ9WrV9drr72mIUOGODscAHB5VC5Q6iQmJuqnn35Sy5Ytdf78eU2fPl2S1KtXLydHBgCQSC5QSs2aNUs///yzPD09FR4erm3btrHYDQBKCKZFAACAqdiKCgAATEVyAQAATEVyAQAATEVyAQAATEVyAZRBU6dOVbNmzWw/Dxo0SFFRUcUex9GjR2WxWLR3795iHxuA85BcAMVo0KBBslgsslgs8vDwUO3atTVhwgRlZGQ4dNzXX39dK1euzNe9JAQAiopzLoBidvfdd2vFihXKysrStm3bNHToUGVkZGjBggV292VlZeV6Qmxh+fv7m9IPAOQHlQugmHl5ealq1aq65ZZb1K9fP/Xv318bNmywTWUsX75ctWvXlpeXlwzD0Pnz5zV8+HAFBQXJz89PHTt21Pfff2/X54wZMxQcHCxfX18NGTJEly9ftnv979MiVqtVr7zyiurWrSsvLy/VqFFDL730kiQpNDRUktS8eXNZLBa1b9/e9r4VK1YoLCxM3t7eatCggebPn283zrfffqvmzZvL29tbERERSkxMNPGbA1BaULkAnMzHx0dZWVmSpF9//VUffPCB1q9fL3d3d0lSjx49VLlyZcXFxcnf31+LFi1Sp06ddPDgQVWuXFkffPCBpkyZorfeekvt2rXT6tWrNW/ePNWuXfuaY8bExGjJkiWaM2eObr/9diUnJ+unn36S9GeC0LJlS33xxRe67bbb5OnpKUlasmSJpkyZojfffFPNmzdXYmKihg0bpgoVKmjgwIHKyMhQz5491bFjR73zzjs6cuSInnzySQd/ewBKJANAsRk4cKDRq1cv2887d+40AgICjAcffNCYMmWK4eHhYaSmptpe//LLLw0/Pz/j8uXLdv3UqVPHWLRokWEYhhEZGWmMHDnS7vVWrVoZTZs2zXPc9PR0w8vLy1iyZEmeMR45csSQZCQmJtq133LLLcZ7771n1/bCCy8YkZGRhmEYxqJFi4zKlSsbGRkZttcXLFiQZ18AyjamRYBitnHjRlWsWFHe3t6KjIzUHXfcoTfeeEOSVLNmTVWpUsV27+7du/XHH38oICBAFStWtF1HjhzRoUOHJEkHDhxQZGSk3Rh///mvDhw4oMzMTHXq1CnfMZ85c0bHjx/XkCFD7OJ48cUX7eJo2rSpypcvn684AJRdTIsAxaxDhw5asGCBPDw8VK1aNbtFmxUqVLC712q1KiQkRJs3b87VT6VKlQo1vo+PT4HfY7VaJf05NdKqVSu7165O3xg8pgjA/0dyARSzChUqqG7duvm6t0WLFkpJSVG5cuVUq1atPO8JCwtTQkKCBgwYYGtLSEi4Zp+33nqrfHx89OWXX2ro0KG5Xr+6xiInJ8fWFhwcrOrVq+vw4cPq379/nv02bNhQq1ev1qVLl2wJzPXiAFB2MS0ClGCdO3dWZGSkoqKi9J///EdHjx7V9u3b9dxzz2nXrl2SpCeffFLLly/X8uXLdfDgQU2ZMkX79u27Zp/e3t6aOHGinn76aa1atUqHDh1SQkKCli1bJkkKCgqSj4+PPv/8c50+fVrnz5+X9OfBXLGxsXr99dd18OBB/fDDD1qxYoVmz54tSerXr5/c3Nw0ZMgQ7d+/X3FxcZo1a5aDvyEAJRHJBVCCWSwWxcXF6Y477tDgwYNVr149PfTQQzp69KiCg4MlSX369NHkyZM1ceJEhYeH69ixYxo1atR1+33++ec1fvx4TZ48WWFhYerTp49SU1MlSeXKldO8efO0aNEiVatWTb169ZIkDR06VEuXLtXKlSvVuHFj3XnnnVq5cqVt62rFihX16aefav/+/WrevLkmTZqkV155xYHfDoCSymIwUQoAAExE5QIAAJiK5AIAAJiK5AIAAJiK5AIAAJiK5AIAAJiK5AIAAJiK5AIAAJiK5AIAAJiK5AIAAJiK5AIAAJiK5AIAAJiK5AIAAJjq/wFkO5k60ifeQgAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 640x480 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "--- Test Your Own Email ---\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter email text:  pawarvrushali393@gmail.com\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Prediction: PHISHING\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.feature_extraction.text import CountVectorizer\n",
    "from sklearn.naive_bayes import MultinomialNB\n",
    "from sklearn.metrics import accuracy_score, confusion_matrix\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Load dataset\n",
    "data = pd.read_csv(\"email.csv\")\n",
    "\n",
    "# Features and labels\n",
    "X = data[\"text\"]\n",
    "y = data[\"label\"]\n",
    "\n",
    "# Split dataset\n",
    "X_train, X_test, y_train, y_test = train_test_split(\n",
    "    X, y, test_size=0.3, random_state=42\n",
    ")\n",
    "\n",
    "# Convert text into numerical features\n",
    "vectorizer = CountVectorizer()\n",
    "\n",
    "X_train_vectors = vectorizer.fit_transform(X_train)\n",
    "X_test_vectors = vectorizer.transform(X_test)\n",
    "\n",
    "# Train model\n",
    "model = MultinomialNB()\n",
    "model.fit(X_train_vectors, y_train)\n",
    "\n",
    "# Predictions\n",
    "predictions = model.predict(X_test_vectors)\n",
    "\n",
    "# Accuracy\n",
    "accuracy = accuracy_score(y_test, predictions)\n",
    "\n",
    "print(\"\\nModel Accuracy:\", round(accuracy * 100, 2), \"%\")\n",
    "\n",
    "# Confusion Matrix\n",
    "cm = confusion_matrix(y_test, predictions, labels=[\"phishing\", \"safe\"])\n",
    "\n",
    "print(\"\\nConfusion Matrix:\")\n",
    "print(cm)\n",
    "\n",
    "# Plot confusion matrix\n",
    "sns.heatmap(\n",
    "    cm,\n",
    "    annot=True,\n",
    "    fmt=\"d\",\n",
    "    xticklabels=[\"phishing\", \"safe\"],\n",
    "    yticklabels=[\"phishing\", \"safe\"]\n",
    ")\n",
    "\n",
    "plt.xlabel(\"Predicted\")\n",
    "plt.ylabel(\"Actual\")\n",
    "plt.title(\"Phishing Email Detection\")\n",
    "plt.show()\n",
    "\n",
    "# User input test\n",
    "print(\"\\n--- Test Your Own Email ---\")\n",
    "\n",
    "email = input(\"Enter email text: \")\n",
    "\n",
    "email_vector = vectorizer.transform([email])\n",
    "\n",
    "result = model.predict(email_vector)\n",
    "\n",
    "print(\"\\nPrediction:\", result[0].upper())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "54ae6533-d0b5-4e36-8539-711277a6d800",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ec02c86f-9bf0-4a2e-b983-6a098f6b6f65",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
