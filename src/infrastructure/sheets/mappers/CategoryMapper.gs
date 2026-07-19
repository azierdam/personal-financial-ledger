class CategoryMapper {
  static toDomain(row) {
    if (!row[0] || !row[1]) throw new MalformedDataException('Invalid Category row');
    return new Category(row[0], row[1]);
  }
  static toRow(category) {
    return [category.categoryId, category.name];
  }
}
