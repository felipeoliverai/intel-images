def load_dataset(path): 

  %%time 

  images = []
  labels = []
  data = []

  for dir in os.listdir(path):
    for file_name in tqdm(os.listdir(os.path.join(path, dir))):

      image_path = os.path.join(path, dir, file_name)
      image = load_img(image_path, target_size=(150, 150, 3), color_mode="rgb")
      image = img_to_array(image)
      image = image.astype("float32")
      image /= 255.0

      images.append(image)
      labels.append(dir)


  dataframe = pd.DataFrame({"Images": images, "Label": labels})
  return dataframe    