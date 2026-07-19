/**
 * Defines the contract for Category storage.
 * Storage-agnostic interface.
 */
interface CategoryRepository {
  /**
   * @param {Category} category
   */
  save(category);
  
  /**
   * @param {string} categoryId
   * @return {Category|null}
   */
  findById(categoryId);
  
  /**
   * @return {Category[]}
   */
  findAll();
  
  /**
   * @param {Category} category
   */
  update(category);
}
