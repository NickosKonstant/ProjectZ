namespace Freecon
{
    using System;
    using System.Collections.Generic;
    using System.ComponentModel.DataAnnotations;
    using System.ComponentModel.DataAnnotations.Schema;
    using System.Data.Entity.Spatial;

    public partial class Member
    {
        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA2214:DoNotCallOverridableMethodsInConstructors")]
        public Member()
        {
            MemberServices = new HashSet<MemberService>();
        }

        [StringLength(40)]
        public string FirstName { get; set; }

        [StringLength(40)]
        public string LastName { get; set; }

        [Key]
        public string userName { get; set; }

        [StringLength(128)]
        public string password { get; set; }

        [StringLength(25)]
        public string email { get; set; }

        public long? phoneNumber { get; set; }

        [StringLength(128)]
        public string Adress { get; set; }

        [StringLength(128)]
        public string Photo { get; set; }

        public int? balance { get; set; }

        [StringLength(500)]
        public string sumary { get; set; }

        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA2227:CollectionPropertiesShouldBeReadOnly")]
        public virtual ICollection<MemberService> MemberServices { get; set; }
    }
}
