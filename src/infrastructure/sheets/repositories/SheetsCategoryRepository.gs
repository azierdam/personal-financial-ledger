class SheetsCategoryRepository {
  constructor(gateway) {
    this.gateway = gateway;
    this.sheetName = 'Categories';
  }

  save(category) {
    this.gateway.appendRow(this.sheetName, CategoryMapper.toRow(category));
  }

  findById(categoryId) {
    const rows = this.gateway.getValues(this.sheetName);
    const row = rows.find(r => r[0] === categoryId);
    return row ? CategoryMapper.toDomain(row) : null;
  }

  findAll() {
    const rows = this.gateway.getValues(this.sheetName);
    return rows.map(r => CategoryMapper.toDomain(r));
  }

  update(category) {
    // Implementation deferred
  }
}
