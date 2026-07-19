/**
 * Defines the contract for Account storage.
 * Storage-agnostic interface.
 */
interface AccountRepository {
  /**
   * @param {Account} account
   */
  save(account);
  
  /**
   * @param {string} accountId
   * @return {Account|null}
   */
  findById(accountId);
  
  /**
   * @return {Account[]}
   */
  findAll();
  
  /**
   * @param {Account} account
   */
  update(account);
}
